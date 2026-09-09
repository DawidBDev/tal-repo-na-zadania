"""Powtórzenie obsługi plików: nazwy względne, brak globalnych loaderów."""
from .common import lesson, theory as T, task as E

# Oryginalne pliki są kopiowane obok notatnika, nie są automatycznie wczytywane.
SOURCE_FILES = {
    3: [(2024, "skrot_przyklad.txt"), (2024, "liczby_przyklad.txt"),
        (2025, "dron_przyklad.txt"), (2025, "dron.txt"), (2025, "symbole_przyklad.txt")],
    5: [(2024, n) for n in ["skrot_przyklad.txt", "skrot2_przyklad.txt", "skrot.txt", "skrot2.txt"]],
    8: [(2024, "liczby_przyklad.txt"), (2024, "liczby.txt")],
    10: [(2025, "symbole_przyklad.txt"), (2025, "symbole.txt")],
    12: [(2025, "dron_przyklad.txt"), (2025, "dron.txt")],
}
EXERCISE_FILES = {
    3: {"demo-liczby.txt": "12\n-3\n7\n"},
    4: {"liczby-trening.txt": "13\n224\n45\n101\n"},
    6: {"czynniki-trening.txt": "2 2 3 5\n12 16 20\n"},
    7: {"fragmenty-trening.txt": "0 0 9 9\n"},
    9: {"symbole-trening.txt": "ooo\nooo\nooo\n***\n"},
    11: {"ruchy-trening.txt": "2 2\n2 2\n2 2\n"},
}

FILE_LESSON = lesson(3, "pliki_tekstowe_i_wyniki", "Powtórzenie: samodzielna praca z plikami",
    "Samodzielne napisanie całego procesu: otwarcie pliku, odczyt, konwersja, obliczenia i zapis odpowiedzi.",
    ["Czym różni się return od print?", "Jak rozpakować parę liczb z listy?",
     "Dlaczego trzeba zachowywać kolejność i powtórzenia rekordów?"],
[
T(1, "Powtórzenie: otwarcie, odczyt i konwersja",
"""Pliki wejściowe leżą obok tego notatnika. Nazwa względna, np. 'demo-liczby.txt', jest liczona względem bieżącego katalogu pracy jądra. Otwórz notatnik z folderu lekcji i uruchom jądro w tym folderze. Jeśli pojawi się FileNotFoundError, sprawdź nazwę, rozszerzenie i katalog pracy; nie obchodź problemu wpisaniem danych ręcznie.

with open(nazwa, 'r', encoding='utf-8') otwiera plik do odczytu i zamyka go po wyjściu z bloku. Iterowanie po pliku daje kolejne wiersze jako napisy. int(wiersz) zamienia zapis liczby na liczbę. W zadaniach sam tworzysz listę oraz kod odczytu — żadna wcześniejsza komórka nie ładuje danych za Ciebie.

Przykład dotyczy wyłącznie małego pliku demonstracyjnego. Zadania wykorzystują inne pliki i różne formaty rekordów.""",
"""liczby_demo = []
with open("demo-liczby.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        liczby_demo.append(int(wiersz))
print(liczby_demo)
assert liczby_demo == [12, -3, 7]"""),
T(3, "Powtórzenie: rekordy i białe znaki",
"""split() dzieli napis po białych znakach; kilka spacji lub tabulator nie tworzy pustych pól. split(' ') zachowuje się inaczej. read() daje cały tekst, readline() jeden wiersz, a read().splitlines() listę wierszy bez zakończeń.

Jeżeli każdy wiersz ma odrębne znaczenie, nie łącz od razu wszystkich liczb w jedną listę. Pary współrzędnych wczytuj wiersz po wierszu i sprawdzaj liczbę pól. strip() usuwa białe znaki z obu końców; rstrip('\\r\\n') usuwa tylko zakończenie wiersza. Wybór zależy od tego, czy spacje są częścią danych.""",
"""wiersz = "  12\\t -5  "
pola_demo = wiersz.split()
assert len(pola_demo) == 2
dx, dy = [int(pole) for pole in pola_demo]
print(dx, dy)
assert (dx, dy) == (12, -5)"""),
T(6, "Powtórzenie: od obliczeń do pliku odpowiedzi",
"""Funkcja obliczeniowa może przyjmować listę, dzięki czemu przetestujesz ją na małych danych. To jednak nie zastępuje programu: w zadaniu plikowym musisz sam otworzyć właściwy plik, wczytać rekordy, wywołać funkcję oraz zapisać odpowiedź.

Tryb 'w' tworzy plik lub zastępuje jego zawartość. Nie zapisuj wyników pod nazwą pliku wejściowego. W tej lekcji zapisuj odpowiedzi obok notatnika, pod nazwą podaną w poleceniu. print(..., file=plik) zapisuje wiersz do pliku. Odczytaj wynik ponownie i sprawdź format oraz liczby, nie tylko komunikat na ekranie.""",
"""with open("demo-wynik.txt", "w", encoding="utf-8") as plik:
    print("Suma:", sum(liczby_demo), file=plik)
with open("demo-wynik.txt", "r", encoding="utf-8") as plik:
    zapis_demo = plik.read()
assert zapis_demo == "Suma: 16\\n"
print(zapis_demo)""")
],
[
E("Białe znaki", "Napisz pola(wiersz), zwracającą listę liczb całkowitych. Obsłuż wielokrotne spacje, tabulatory i pusty wiersz.",
  "def pola(wiersz):\n    return [int(x) for x in wiersz.split()]",
  'assert pola("  12\\t -3  0 ") == [12, -3, 0]\nassert pola("  ") == []',
  "Przypomnij sobie różnicę między split() i split(' ')."),
E("Samodzielne wczytanie jednej kolumny", "Plik skrot_przyklad.txt zawiera jedną liczbę w każdym wierszu. Napisz czytaj_liczby(nazwa): sam otwórz plik i wczytaj liczby. Wywołaj ją dla tego pliku, zapisz listę w a. Sprawdź liczbę rekordów oraz pierwszy i ostatni element. Nie przepisuj danych do kodu.",
  'def czytaj_liczby(nazwa):\n    liczby = []\n    with open(nazwa, "r", encoding="utf-8") as plik:\n        for wiersz in plik:\n            liczby.append(int(wiersz))\n    return liczby\na = czytaj_liczby("skrot_przyklad.txt")',
  "assert (len(a), a[0], a[-1]) == (20, 18067, 285)",
  "Odczyt zwraca tekst; konwersja jest częścią Twojego rozwiązania."),
E("Dwa wiersze, dwa znaczenia", "Napisz dwa_wiersze(nazwa). Sam otwórz liczby_przyklad.txt, odczytaj dwa wiersze i zwróć dwie listy liczb. Zapisz je w a i b. Pierwszy wiersz to czynniki, drugi to liczby do zbadania. Potwierdź 200 i 20 elementów.",
  'def dwa_wiersze(nazwa):\n    with open(nazwa, "r", encoding="utf-8") as plik:\n        wiersze = plik.read().splitlines()\n    assert len(wiersze) == 2\n    return pola(wiersze[0]), pola(wiersze[1])\na, b = dwa_wiersze("liczby_przyklad.txt")',
  "assert (len(a), len(b)) == (200, 20)", "Nie spłaszczaj dwóch rekordów do jednej listy."),
E("Pary przesunięć", "Napisz czytaj_pary(nazwa), samodzielnie otwierającą plik i wymagającą dwóch liczb w każdym wierszu. Wczytaj dron_przyklad.txt do r. Potwierdź 10 par, pierwszą (2000,1001) i ostatnią (2000,-1006).",
  'def czytaj_pary(nazwa):\n    wynik = []\n    with open(nazwa, "r", encoding="utf-8") as plik:\n        for numer, wiersz in enumerate(plik, 1):\n            rekord = pola(wiersz)\n            assert len(rekord) == 2, f"Wiersz {numer}: oczekiwano dwóch pól"\n            wynik.append(tuple(rekord))\n    return wynik\nr = czytaj_pary("dron_przyklad.txt")',
  "assert (len(r), r[0], r[-1]) == (10, (2000, 1001), (2000, -1006))",
  "Konwertuj i sprawdzaj osobno każdy wiersz."),
E("Odczyt i kontrola alfabetu", "Napisz bledne_wiersze(napisy), zwracającą numery od 1 napisów o długości innej niż 12 lub ze znakiem spoza o,+,*. Następnie sam otwórz symbole_przyklad.txt, wczytaj napisy bez zakończeń wierszy do napisy i sprawdź cały plik.",
  'def bledne_wiersze(napisy):\n    return [i for i, s in enumerate(napisy, 1)\n            if len(s) != 12 or any(c not in "o+*" for c in s)]\nwith open("symbole_przyklad.txt", "r", encoding="utf-8") as plik:\n    napisy = [wiersz.rstrip("\\r\\n") for wiersz in plik]',
  'assert bledne_wiersze(["o"*12, "+x"+"o"*10, "*"]) == [2, 3]\nassert len(napisy) == 20\nassert bledne_wiersze(napisy) == []',
  "Nie usuwaj ostatniego symbolu razem z końcem wiersza."),
E("Raport o parach", "Napisz bilans(ruchy), zwracającą (liczba_ruchow, suma_dx, suma_dy). Korzystając z własnego czytaj_pary, wczytaj ponownie dron_przyklad.txt i oblicz bilans_przykladu.",
  'def bilans(ruchy):\n    sx = sy = 0\n    for dx, dy in ruchy:\n        sx += dx\n        sy += dy\n    return len(ruchy), sx, sy\nbilans_przykladu = bilans(czytaj_pary("dron_przyklad.txt"))',
  "assert bilans_przykladu == (10, 20000, 0)", "Do obliczeń przekazuj dane, nie nazwę pliku."),
E("Samodzielny zapis i kontrola", "Napisz zapisz_liczby(nazwa, liczby): sam otwórz plik do zapisu i zapisz po jednej liczbie na wiersz. Zapisz [7,7,2] do test-liczb.txt i wczytaj własnym czytaj_liczby. Sprawdź też pustą listę, bez nadpisywania plików wejściowych.",
  'def zapisz_liczby(nazwa, liczby):\n    with open(nazwa, "w", encoding="utf-8") as plik:\n        for n in liczby:\n            print(n, file=plik)\nzapisz_liczby("test-liczb.txt", [7, 7, 2])\nodczyt_zapisu = czytaj_liczby("test-liczb.txt")\nzapisz_liczby("test-pusty.txt", [])\npusty_odczyt = czytaj_liczby("test-pusty.txt")',
  "assert odczyt_zapisu == [7, 7, 2]\nassert pusty_odczyt == []",
  "Dwa wystąpienia 7 muszą pozostać dwoma wierszami."),
E("Cały proces na pełnym pliku", "Sam wczytaj dron.txt, używając własnego kodu, oblicz bilans i zapisz raport-dron.txt: trzy wiersze z podpisami ruchy, x, y. Odczytaj go ponownie do odczyt_raportu. Wartości muszą wynikać z danych, a nie z przepisania oczekiwanej odpowiedzi.",
  'liczba, sx, sy = bilans(czytaj_pary("dron.txt"))\nwith open("raport-dron.txt", "w", encoding="utf-8") as plik:\n    print("ruchy", liczba, file=plik)\n    print("x", sx, file=plik)\n    print("y", sy, file=plik)\nwith open("raport-dron.txt", "r", encoding="utf-8") as plik:\n    odczyt_raportu = plik.read()',
  'assert (liczba, sx, sy) == (100, 20000, 0)\nassert odczyt_raportu == "ruchy 100\\nx 20000\\ny 0\\n"',
  "Kompletne rozwiązanie obejmuje odczyt, obliczenia i zapis."),
E("Samodzielnie: pierwszy błędny rekord", "Napisz pierwszy_blad(wiersze), zwracającą numer pierwszego wiersza niebędącego parą liczb całkowitych. Obsłuż ValueError. Dla poprawnych danych zwróć None.",
  'def pierwszy_blad(wiersze):\n    for i, w in enumerate(wiersze, 1):\n        try:\n            dane = pola(w)\n        except ValueError:\n            return i\n        if len(dane) != 2:\n            return i\n    return None',
  'assert pierwszy_blad(["1 2", "x 3"]) == 2\nassert pierwszy_blad(["1 2", "3 4"]) is None',
  "Zła liczba pól i tekst zamiast liczby to różne błędy."),
E("Samodzielnie: od pliku do indeksów palindromów", "W nowej komórce sam otwórz symbole_przyklad.txt i wczytaj napisy. Zapisz w numery_palindromow numery wierszy będących palindromami, licząc od 1. Nie polegaj na liście utworzonej wcześniej.",
  'with open("symbole_przyklad.txt", "r", encoding="utf-8") as plik:\n    napisy_do_palindromow = [w.rstrip("\\r\\n") for w in plik]\nnumery_palindromow = [i for i, s in enumerate(napisy_do_palindromow, 1) if s == s[::-1]]',
  "assert numery_palindromow == [5]", "Numer wiersza i indeks listy nie są tym samym.")
])
