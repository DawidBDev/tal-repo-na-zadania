"""Weryfikacja osobnych lekcji, samodzielnego I/O i publikacji bez kluczy."""
import ast
import contextlib
import hashlib
import io
import itertools
import json
import math
import os
import random
import re
import shutil
import sys
import tempfile
import zipfile
from fractions import Fraction
from pathlib import Path

try:
    import nbformat
    from nbclient import NotebookClient
except ImportError:
    sys.exit("Zainstaluj: python -m pip install nbformat nbclient ipykernel")

from content.files import SOURCE_FILES, EXERCISE_FILES

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT.parent / "prezentacja-python"
NOTEBOOKS = sorted(ROOT.glob("[0-9][0-9]_*/karta_pracy.ipynb"))
TEACHER_NOTEBOOKS = [ROOT / "materialy-prowadzacego" / p.parent.name / "rozwiazania.ipynb"
                     for p in NOTEBOOKS]
OFFICIAL = {5: "2024_zadanie_3.md", 8: "2024_zadanie_4.md",
            10: "2025_zadanie_2.md", 12: "2025_zadanie_3.md"}


def check_structure(path, number, teacher=False):
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    meta = nb.metadata.course
    assert meta.number == number
    assert meta.variant == ("teacher" if teacher else "student")
    assert "minutes" not in meta and "task_minutes" not in meta
    assert len({c.id for c in nb.cells}) == len(nb.cells)
    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    for tag, count in [("exercise", 8), ("homework", 2), ("solution", 10 if teacher else 0)]:
        assert sum(tag in c.metadata.get("tags", []) for c in code_cells) == count
    for cell in nb.cells:
        assert not re.search(r"(około \d+ min|60 minut|[·] \d+ minut)", cell.source)
        assert not any(token in cell.source for token in ["DANE /", "WYNIKI /", "KATALOG_KURSU"])
        if not teacher:
            assert cell.metadata.presentation.kind != "solution"
        if cell.cell_type != "code":
            continue
        assert cell.execution_count is None and cell.outputs == []
        tree = ast.parse(cell.source)
        if cell.metadata.presentation.kind in {"exercise", "homework", "recall"}:
            assert not tree.body, "Komórki robocze mają być puste."
        if cell.metadata.presentation.kind == "solution":
            assert any(isinstance(node, ast.Assert) for node in ast.walk(tree))
        if not teacher:
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "open":
                    # Jedyny aktywny odczyt w wersji ucznia to jawny przykład na osobnym pliku demo.
                    assert number == 3 and isinstance(node.args[0], ast.Constant)
                    assert node.args[0].value in {"demo-liczby.txt", "demo-wynik.txt"}
    if number in OFFICIAL:
        original = (ROOT / "tresci-maturalne" / OFFICIAL[number]).read_text(encoding="utf-8")
        original = original.replace("materialy-zrodlowe/", "").strip()
        quoted = "\n".join(c.source for c in nb.cells if c.metadata.presentation.kind == "matura")
        assert all(p in quoted for p in original.split("\n\n"))
        assert (path.parent / f"arkusz-{OFFICIAL[number][:4]}.pdf").is_file()
    for year, name in SOURCE_FILES.get(number, []):
        assert (path.parent / name).read_bytes() == (ROOT / "dane" / str(year) / name).read_bytes()
    for name, text in EXERCISE_FILES.get(number, {}).items():
        assert (path.parent / name).read_text(encoding="utf-8") == text
    if teacher and number >= 3:
        assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "open"
                   for cell in code_cells if cell.metadata.presentation.kind == "solution"
                   for node in ast.walk(ast.parse(cell.source)))
    return nb


def expected_sections(notebook):
    result = []
    for cell in notebook.cells:
        p = cell.metadata.presentation
        assert p.kind != "solution"
        content = cell.source.strip()
        if cell.cell_type == "code":
            content = chr(96)*3 + "python\n" + content + "\n" + chr(96)*3
        if result and result[-1]["id"] == p.section:
            result[-1]["markdown"] += "\n\n" + content
        else:
            result.append(dict(id=p.section, title=p.title, kind=p.kind, context="", markdown=content))
    return result


def check_public_zip(path, expected):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(expected), path
        assert len(archive.namelist()) == len(expected)
        for name, source in expected.items():
            assert archive.read(name) == source.read_bytes()
            assert not any(part in name.lower() for part in ["rozwiazania", "kartkowki", "prowadzacego"])
            assert not name.endswith((".py", ".cpp", ".mjs"))
            if name.endswith(".ipynb"):
                nb = json.loads(archive.read(name))
                assert nb["metadata"]["course"]["variant"] == "student"
                assert all(c["metadata"]["presentation"]["kind"] != "solution" for c in nb["cells"])


def check_site(notebooks):
    assert (SITE / "index.html").is_file()
    raw = (SITE / "slides-data.js").read_text(encoding="utf-8")
    course = json.loads(raw.removeprefix("window.PYTHON_COURSE = ").strip().removesuffix(";"))
    assert course["meta"]["lessonCount"] == len(notebooks) == 12
    assert [l["number"] for l in course["lessons"]] == list(range(13))
    assert course["lessons"][0]["kind"] == "organization"
    assert course["meta"]["taskCount"] == 120
    assert all(s["kind"] != "solution" for l in course["lessons"] for s in l["sections"])
    assert "60 minut" not in raw and "około " not in raw
    org = "00_organizacja_i_zasady_zajec.md"
    assert (SITE / org).read_bytes() == (ROOT / org).read_bytes()
    assert len(list(SITE.rglob("*.ipynb"))) == 12
    assert not list(SITE.rglob("*.cpp")) and not list(SITE.rglob("*.py"))
    assert not list(SITE.rglob("*kartkowki*")) and not list(SITE.rglob("*rozwiazania*"))
    for legacy in ["karty", "dane", "materialy-zrodlowe"]:
        assert not (SITE / legacy).exists(), "Stary katalog publikacji: " + legacy
    all_files = {"kurs-python/README.md": ROOT / "README.md", "kurs-python/" + org: ROOT / org}
    for path, nb, lesson in zip(NOTEBOOKS, notebooks, course["lessons"][1:]):
        assert lesson["number"] == nb.metadata.course.number
        assert (SITE / lesson["notebook"]).read_bytes() == path.read_bytes()
        assert lesson["checksum"] == hashlib.sha256(path.read_bytes()).hexdigest()
        assert lesson["sections"] == expected_sections(nb)
        assets = [path, path.parent / "README.md"] + [path.parent / name for name in nb.metadata.course.inputs]
        if lesson["number"] in OFFICIAL:
            assets.append(path.parent / f"arkusz-{OFFICIAL[lesson['number']][:4]}.pdf")
        zip_files = {}
        for file in assets:
            relative = path.parent.name + "/" + file.name
            assert (SITE / "lekcje" / relative).read_bytes() == file.read_bytes()
            zip_files[relative] = file
            all_files["kurs-python/" + relative] = file
        check_public_zip(SITE / lesson["download"], zip_files)
    check_public_zip(SITE / "kurs-python.zip", all_files)
    print("OK: lekcja 0, 12 kart, dane przy kartach, zgodne slajdy i 13 ZIP-ów bez kluczy.")


def check_quizzes():
    text = (ROOT / "materialy-prowadzacego" / "kartkowki_01-12.md").read_text(encoding="utf-8")
    questions, answers = text.split("## Klucz odpowiedzi", 1)
    assert re.findall(r"^## Przed lekcją (\d+)", questions, re.M) == [str(i) for i in range(1, 13)]
    assert re.findall(r"^### Przed lekcją (\d+)", answers, re.M) == [str(i) for i in range(1, 13)]
    for section in re.split(r"^## Przed lekcją ", questions, flags=re.M)[1:]:
        assert re.findall(r"^([1-3])[.] ", section, re.M) == ["1", "2", "3"]
    assert "10 minut" in questions
    # Niezależna kontrola wartości wykorzystanych w pytaniach i kluczu.
    assert (17//5, 17%5, 17/5) == (3, 2, 3.4)
    assert sum(n for n in range(1, 7) if n % 2 == 0) == 12
    assert sum(n*n for n in range(1, 6)) == 55
    assert int("10110", 2) == 22 and math.gcd(84, 35) == 7
    assert math.gcd(77, 77) == 77
    assert sorted([2,4,2,3,3,4], reverse=True)[1] == 4
    assert Fraction(19,3) > Fraction(10,2)
    assert int("102",3) == 11 and 2*int("22",3) == int("121",3)
    print("OK: 12 kartkówek, 36 pytań z kluczem; pytania nie są publikowane.")


def algorithm_checks(scopes):
    rng = random.Random(2026)
    skrot = scopes[5]["skrot"]
    for n in range(1, 10000):
        expected = int("".join(c for c in str(n) if c in "13579") or "0")
        assert skrot(n) == expected
    source = next(c.source for c in nbformat.read(TEACHER_NOTEBOOKS[4], 4).cells
                  if c.cell_type == "code" and c.source.startswith("def skrot("))
    function = ast.parse(source).body[0]
    assert not any(isinstance(n, (ast.Call, ast.List, ast.Dict, ast.Set, ast.Div))
                   or isinstance(n, ast.Constant) and not isinstance(n.value, int)
                   for n in ast.walk(function))

    def best_reference(a, minimum):
        candidates = [(Fraction(sum(a[l:r]), r-l), -l, -(r-l), sum(a[l:r]))
                      for l in range(len(a)-minimum+1)
                      for r in range(l+minimum, len(a)+1)]
        _, negative_start, negative_length, total = max(candidates)
        return total, -negative_length, -negative_start

    for _ in range(200):
        a = [rng.randrange(-20, 30) for _ in range(rng.randrange(1, 15))]
        k = rng.randint(1, len(a))
        assert scopes[8]["z44"](a, k) == best_reference(a, k)
    assert scopes[8]["odp"]["4.4"] == (73243, 61, 1847)
    for _ in range(100):
        factors = [rng.choice([2, 3, 5, 7]) for _ in range(rng.randrange(1, 8))]
        possible = {math.prod(items) for size in range(len(factors)+1)
                    for items in itertools.combinations(factors, size)}
        candidates = list(range(2, 101))
        assert scopes[8]["z43"](factors, candidates) == [n for n in candidates if n in possible]

    for _ in range(100):
        height, width = rng.randrange(1, 8), rng.randrange(1, 8)
        grid = ["".join(rng.choice("oo+") for _ in range(width)) for _ in range(height)]
        expected = []
        for r in range(height-2):
            for c in range(width-2):
                square = "".join(row[c:c+3] for row in grid[r:r+3])
                if len(set(square)) == 1:
                    expected.append((r+2, c+2))
        assert scopes[10]["z22"](grid) == expected
    translate = str.maketrans("o+*", "012")
    for n in range(3000):
        assert int(scopes[10]["koduj"](n).translate(translate), 3) == n
    symbols = scopes[10]["napisy"]
    assert scopes[10]["odp"]["2.1"] == [
        "++o+o++o+o++", "+*+**++**+*+", "*+o++**++o+*",
        "*oo*o**o*oo*", "+*++*oo*++*+", "+o++oooo++o+"]
    values = [int(s.translate(translate), 3) for s in symbols]
    assert sum(values) == scopes[10]["odp"]["2.4"][0]
    assert max(values) == scopes[10]["odp"]["2.3"][0]

    for _ in range(100):
        points = [(x, rng.randrange(-5, 6)) for x in range(rng.randrange(3, 15))]
        expected = [(a, m, c) for a, m, c in itertools.combinations(points, 3)
                    if tuple(2*z for z in m) == tuple(x+y for x, y in zip(a, c))]
        assert sorted(scopes[12]["z32b"](points)) == sorted(expected)
    movements = scopes[12]["ruchy"]
    assert sum(math.gcd(x, y) > 1 for x, y in movements) == 40
    print("OK: niezależne testy skrótu, ułamków, czynników, siatek, konwersji i geometrii.")


def main():
    assert len(NOTEBOOKS) == 12
    assert not list(ROOT.glob("[0-9][0-9]_*.ipynb")), "Usuń stare karty z głównego katalogu."
    students = [check_structure(path, i) for i, path in enumerate(NOTEBOOKS, 1)]
    teachers = [check_structure(path, i, teacher=True) for i, path in enumerate(TEACHER_NOTEBOOKS, 1)]
    for student, teacher in zip(students, teachers):
        assert student.cells == teacher.cells[:len(student.cells)]
    check_site(students)
    check_quizzes()
    scopes = {}
    old_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="python-course-validation-") as temporary:
        try:
            for number, (student_path, student, teacher_path, teacher) in enumerate(
                    zip(NOTEBOOKS, students, TEACHER_NOTEBOOKS, teachers), 1):
                for variant, path, nb in [("student", student_path, student), ("teacher", teacher_path, teacher)]:
                    work = Path(temporary) / f"{number:02d}-{variant}"
                    work.mkdir()
                    snapshots = {}
                    for name in nb.metadata.course.inputs:
                        source = path.parent / name
                        shutil.copy2(source, work / name)
                        snapshots[name] = source.read_bytes()
                    NotebookClient(nb, timeout=120, kernel_name="python3",
                                   resources={"metadata": {"path": str(work)}}).execute()
                    assert all((work / name).read_bytes() == data for name, data in snapshots.items())
                    if variant == "teacher":
                        successes = sum("Testy zadania " in output.get("text", "")
                                        for c in nb.cells if c.cell_type == "code"
                                        for output in c.outputs if output.output_type == "stream")
                        assert successes == 10
                        scope = {"__name__": "__main__"}
                        os.chdir(work)
                        with contextlib.redirect_stdout(io.StringIO()):
                            for cell in nb.cells:
                                if cell.cell_type == "code":
                                    exec(compile(cell.source, f"{path}:{cell.id}", "exec"), scope)
                        scopes[number] = scope
                        if number >= 3:
                            assert list(work.glob("wyniki*.txt")) or (work / "raport-dron.txt").is_file()
                print(f"OK: lekcja {number:02d} — dwa świeże jądra, własny katalog i testy.", flush=True)
            algorithm_checks(scopes)
        finally:
            os.chdir(old_cwd)
    print("WYNIK: 12 kart ucznia, 12 kluczy, 120 rozwiązań, 36 pytań; publikacja bez kluczy.")


if __name__ == "__main__":
    main()
