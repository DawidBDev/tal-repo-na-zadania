from .common import lesson, theory as T, task as E

LESSONS = [
lesson(9, 'napisy_system_trojkowy_i_siatki', 'Zapis pozycyjny, palindromy i siatki znaków',
'Przygotowanie każdego algorytmu do zadania 2 matury 2025.',
["Dlaczego '*' w danych jest znakiem, a w kodzie może być operatorem?", 'Co daje Horner dla cyfr 1,0,2 w podstawie 3?', 'Jakie indeksy opisują środkowe pole bloku 3×3?'],
[
T(1, 'Znaczenie symbolu i porównywanie napisów',
"""Alfabet danych o,+,* koduje wartości 0,1,2. Słownik {'o':0,'+':1,'*':2} oddziela wygląd znaku od jego wartości. Pojedynczy znak jest w Pythonie napisem długości 1.

Porównanie napisów działa według porządku znaków, który nie musi odpowiadać wartości liczby. Największy napis przez max(napisy) nie musi oznaczać największej zakodowanej liczby. Palindrom z kolei zależy wyłącznie od symetrii znaków, a nie od wartości liczbowej.""",
"""cyfra = {"o": 0, "+": 1, "*": 2}
print([cyfra[c] for c in "+o*"])
print(max(["o", "*"]))  # to nie maksimum wartości 0 i 2
assert "o" > "*" """),
T(3, 'Systemy pozycyjne w obie strony',
"""Przy odczycie od lewej stosuj wynik = wynik*3 + cyfra. Przy zapisie liczby bierz reszty z dzielenia przez 3, zamieniaj na symbole i odwróć kolejność. Dla zera wynikiem jest o.

Zera wiodące nie zmieniają wartości. Przekształcenie napis→liczba→napis usuwa zera wiodące, więc nie musi odtwarzać oryginalnego napisu. Natomiast liczba→napis→liczba zawsze powinna odtwarzać nieujemną liczbę. Suma 2000 wartości może potrzebować więcej niż 12 znaków.""",
"""wynik = 0
for c in "+o*":
    wynik = wynik * 3 + {"o": 0, "+": 1, "*": 2}[c]
assert wynik == 11
print("Maksimum dla 12 cyfr:", 3**12 - 1)"""),
T(6, 'Siatka: indeksy i nakładające się okna',
"""Lista napisów opisuje prostokątną tablicę: wiersze[r][c] to znak w wierszu r i kolumnie c. Dla wysokości h i szerokości w lewe górne rogi bloków 3×3 mają r w range(h-2), c w range(w-2).

Bloki mogą się nakładać i każdy należy policzyć. Dla rogu (r,c) środek ma indeksy (r+1,c+1), czyli numerację od 1 równą (r+2,c+2). Najpierw sprawdź wszystkie dziewięć znaków, dopiero potem dopisz środek.""",
"""wiersze = ["oooo", "oooo", "oooo"]
print(wiersze[1][2])
print("Liczba możliwych bloków:", (len(wiersze)-2)*(len(wiersze[0])-2))
assert (len(wiersze)-2)*(len(wiersze[0])-2) == 2"""),
],
[
E('Mapowanie symboli',
"Napisz cyfry(s), zamieniającą napis z alfabetu o,+,* na listę wartości. Dla '+o*+': [1,0,2,1].",
"""def cyfry(s):
    mapa = {"o": 0, "+": 1, "*": 2}
    return [mapa[c] for c in s]""",
'assert cyfry("+o*+") == [1, 0, 2, 1]',
'Nie porównuj kodów znaków z ich wartościami.'),
E('Palindrom i ostatni znak',
"Napisz palindrom(s) porównującą symetryczne indeksy. Sprawdź 'o++o', 'o++*' oraz jednoznakowy napis. Dlaczego pominięcie ostatniego znaku zmienia wynik?",
"""def palindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True""",
"""assert palindrom("o++o")
assert not palindrom("o++*")
assert palindrom("o")""",
'Prawy indeks dla i=0 to -1, a nie -2.'),
E('Zapis symboliczny na liczbę',
"Napisz dekoduj(s) metodą Hornera. Dla '+o*' wynik 11, dla 'oo+o*' również 11. Nie pomijaj ostatniego symbolu.",
"""def dekoduj(s):
    wynik = 0
    for c in cyfry(s):
        wynik = wynik*3 + c
    return wynik""",
"""assert dekoduj("+o*") == 11
assert dekoduj("oo+o*") == 11
assert dekoduj("*") == 2""",
'Przechodź po wszystkich znakach napisu, bez skracania długości.'),
E('Liczba na zapis symboliczny',
"Napisz koduj(n), n>=0. Dla 0: 'o', 5: '+*', 26: '***'. Sprawdź odwracalność dla n od 0 do 100.",
"""def koduj(n):
    if n == 0:
        return "o"
    odwrotnie = []
    while n > 0:
        odwrotnie.append("o+*"[n % 3])
        n //= 3
    return "".join(odwrotnie[::-1])""",
"""assert koduj(0) == "o"
assert koduj(5) == "+*"
assert koduj(26) == "***"
for n in range(101):
    assert dekoduj(koduj(n)) == n""",
'Nie ograniczaj długości wyniku do długości napisów wejściowych.'),
E('Maksimum z właściwym kluczem',
'Napisz najwiekszy(napisy), zwracającą parę (wartość,oryginalny napis). W razie remisu wybierz pierwszy. Załóż listę niepustą.',
"""def najwiekszy(napisy):
    napis = max(napisy, key=dekoduj)
    return dekoduj(napis), napis""",
"""assert najwiekszy(["o", "*", "+"]) == (2, "*")
assert najwiekszy(["oo+", "+"]) == (1, "oo+")""",
'key pozwala porównywać wartość, zachowując oryginalny napis.'),
E('Jeden blok 3×3',
'Napisz jednolity(wiersze,r,c), sprawdzającą dziewięć pól bloku o podanym lewym górnym rogu. Załóż, że blok mieści się w siatce.',
"""def jednolity(wiersze, r, c):
    znak = wiersze[r][c]
    for dr in range(3):
        for dc in range(3):
            if wiersze[r+dr][c+dc] != znak:
                return False
    return True""",
"""assert jednolity(["ooo", "ooo", "ooo"], 0, 0)
assert not jednolity(["ooo", "o+o", "ooo"], 0, 0)""",
'Zwróć True dopiero po przejściu wszystkich dziewięciu pól.'),
E('Wszystkie środki',
"Napisz kwadraty(wiersze) dla prostokątnej siatki, zwracającą środki w numeracji od 1. Dla trzech wierszy 'oooo' wynik to [(2,2),(2,3)]. Dla za małej siatki zwróć [].",
"""def kwadraty(wiersze):
    if len(wiersze) < 3 or len(wiersze[0]) < 3:
        return []
    return [(r+2, c+2) for r in range(len(wiersze)-2)
            for c in range(len(wiersze[0])-2) if jednolity(wiersze, r, c)]""",
"""assert kwadraty(["oooo"]*3) == [(2, 2), (2, 3)]
assert kwadraty(["oo"]*2) == []
assert kwadraty([]) == []""",
'Nie przeskakuj o trzy kolumny po znalezieniu kwadratu.'),
E('Małe zadanie łączące',
'Sam otwórz symbole-trening.txt i wczytaj jego wiersze do napisy, bez zakończeń wierszy. Używając własnych funkcji, zbuduj raport: palindromy, środki kwadratów, maksimum i suma w obu zapisach. Następnie sam zapisz te cztery części w wyniki-trening.txt. Nie przepisuj zawartości pliku do kodu.',
"""with open("symbole-trening.txt", "r", encoding="utf-8") as plik:
    napisy = [wiersz.rstrip("\\r\\n") for wiersz in plik]
suma = sum(dekoduj(s) for s in napisy)
raport = {"palindromy": [s for s in napisy if palindrom(s)],
          "kwadraty": kwadraty(napisy), "maksimum": najwiekszy(napisy),
          "suma": (suma, koduj(suma))}
with open("wyniki-trening.txt", "w", encoding="utf-8") as plik:
    for nazwa, wynik in raport.items():
        print(nazwa, wynik, file=plik)""",
'assert raport == {"palindromy": napisy, "kwadraty": [(2,2)], "maksimum": (26,"***"), "suma": (26,"***")}',
'To te same rodzaje wyników, które złożysz na kolejnej karcie.'),
E('Samodzielnie: inne systemy',
'Napisz wartosc(s,p) dla alfabetu 0123456789ABCDEF i 2<=p<=16. Sprawdzaj dopuszczalność cyfr. Użyj int(s,p) tylko do testów.',
"""def wartosc(s, p):
    alfabet = "0123456789ABCDEF"
    wynik = 0
    for znak in s:
        cyfra = alfabet.index(znak)
        assert cyfra < p
        wynik = wynik*p + cyfra
    return wynik""",
"""assert wartosc("1011",2) == 11
assert wartosc("FF",16) == 255
assert wartosc("17",8) == int("17",8)""",
'Ten sam Horner działa dla dowolnej podstawy.'),
E('Samodzielnie: zero wiodące',
"Napisz kanoniczny(s) przez dekodowanie i ponowne kodowanie. 'ooo+o' ma dać '+o', 'ooo' ma dać 'o'. Wyjaśnij, dlaczego nie odtwarzasz całego oryginału.",
"""def kanoniczny(s):
    return koduj(dekoduj(s))""",
"""assert kanoniczny("ooo+o") == "+o"
assert kanoniczny("ooo") == "o"
""",
'Wartość liczby nie przechowuje informacji o zerach wiodących.'),
], official=None),
lesson(10, 'matura_2025_zadanie_2_zapis_symboliczny', 'Matura 2025: Zapis symboliczny krok po kroku',
'Pełne rozwiązanie podpunktów 2.1–2.4, z kontrolą indeksów, powtórzeń i zapisu wyniku.',
['Ile znaków ma każdy rekord w symbole.txt?', 'Czy sumę należy ograniczyć do dwunastu symboli?', 'Co oznacza para (6,3) w odpowiedzi do 2.2?'],
[
T(1, 'Najpierw format, potem własność',
"""Każdy wiersz zawiera dokładnie 12 symboli. splitlines usuwa zakończenia wierszy, zachowując wszystkie znaki rekordu. Nie zmniejszaj długości napisu ręcznie o jeden: po splitlines ostatni symbol jest już zwykłą daną.

W 2.1 wypisujemy palindromy w oryginalnej kolejności, po jednym na wiersz. Lista wynikowa jest odpowiednia; set usunąłby powtarzające się rekordy.""",
"""wiersz = "oooo+**+oooo\\r\\n"
napis = wiersz.rstrip("\\r\\n")
assert len(napis) == 12
assert napis == napis[::-1]
print(napis)"""),
T(3, 'Sprawdzenie bloku i całej planszy',
"""W 2.2 wystarczy przeglądać możliwe środki albo rogi. Wybierz jedną konwencję i konsekwentnie przelicz wynik na numerację od 1. Ostatni dopuszczalny blok kończy się na ostatnim wierszu i ostatniej kolumnie.

Przykład sześciu wierszy w treści CKE jest inny niż pierwszych sześć wierszy pliku symbole_przyklad.txt. Obydwa przykłady są potrzebne: ręczna plansza sprawdza nakładanie kwadratów, plik sprawdza cały odczyt.""",
"""siatka = ["+++","+++","+++"]
r, c = 0, 0
srodek_od_1 = (r+2, c+2)
assert srodek_od_1 == (2,2)
print(srodek_od_1)"""),
T(6, 'Suma i pełne rozwiązanie',
"""Dla każdej wartości wykonaj jeden odczyt symboli. Python int nie ma stałej granicy 32-bitowej, a więc nie wymaga specjalnego typu do sumy. Wygodnie oddzielić dekodowanie, kodowanie i raport.

Ostateczny raport ma cztery podpisane części. Dla 2.2 wypisz liczbę kwadratów, a następnie współrzędne każdego środka. Dla 2.3 zachowaj oryginalny napis największej liczby, w tym zera wiodące, jeżeli by występowały.""",
"""maksymalny_rekord = 3**12 - 1
print(maksymalny_rekord, 2000 * maksymalny_rekord)
assert maksymalny_rekord == 531440"""),
],
[
E('Odczyt przykładów',
'Napisz wczytaj(nazwa). Sam otwórz symbole_przyklad.txt, usuń tylko zakończenia wierszy i zwróć listę napisów. Sprawdź długość 12 i alfabet o,+,* każdego rekordu. Zapisz listę w napisy_p.',
"""def wczytaj(nazwa):
    with open(nazwa, "r", encoding="utf-8") as plik:
        napisy = [wiersz.rstrip("\\r\\n") for wiersz in plik]
    assert all(len(s) == 12 and all(c in "o+*" for c in s) for s in napisy)
    return napisy
napisy_p = wczytaj("symbole_przyklad.txt")""",
"""assert len(napisy_p) == 20
assert napisy_p[0] == "+**+o*o++*o+"
""",
'Nie usuwaj ostatniego symbolu przez s[:-1].'),
E('2.1: palindromy',
'Napisz z21(napisy), zachowującą kolejność i powtórzenia. Porównaj z odpowiedzią CKE dla pliku przykładowego.',
"""def z21(napisy):
    return [s for s in napisy if s == s[::-1]]""",
"""assert z21(napisy_p) == ["oooo+**+oooo"]
assert z21(["oo", "oo", "o+"]) == ["oo", "oo"]""",
'Pętla po liście pozwala zachować kolejność pliku.'),
E('2.2: funkcja i przykład ręczny',
'Napisz z22(wiersze). Uruchom na sześciu wierszach z treści CKE. Wynik: [(3,5),(3,6),(4,11)]. Następnie na pliku przykładowym: [(6,3)].',
"""def z22(wiersze):
    wynik = []
    for r in range(len(wiersze)-2):
        for c in range(len(wiersze[0])-2):
            znak = wiersze[r][c]
            if all(wiersze[r+dr][c+dc] == znak for dr in range(3) for dc in range(3)):
                wynik.append((r+2,c+2))
    return wynik

reczne = ["+**+o*o++*o+", "+++oooo*o***", "+o*oooo**+++",
          "*+*oooooo+++", "o**o+++o++++", "oooo++**+*+o"]""",
"""assert z22(reczne) == [(3,5),(3,6),(4,11)]
assert z22(napisy_p) == [(6,3)]""",
'Dwa pierwsze kwadraty nakładają się.'),
E('2.3: Horner i maksimum',
"Napisz dekoduj(s) i z23(napisy), która zwraca parę (wartość,napis). Sprawdź (519789,'***+o*ooo++o').",
"""def dekoduj(s):
    wynik = 0
    mapa = {"o":0, "+":1, "*":2}
    for c in s:
        wynik = wynik*3 + mapa[c]
    return wynik

def z23(napisy):
    napis = max(napisy, key=dekoduj)
    return dekoduj(napis), napis""",
"""assert z23(napisy_p) == (519789, "***+o*ooo++o")
assert dekoduj("*") == 2""",
'Przejdź po wszystkich dwunastu symbolach.'),
E('2.4: suma i zapis odwrotny',
'Napisz koduj(n) i z24(napisy), zwracającą (suma,zakodowana suma). Sprawdź oba wyniki z przykładu CKE.',
"""def koduj(n):
    if n == 0:
        return "o"
    wynik = ""
    while n > 0:
        wynik = "o+*"[n%3] + wynik
        n //= 3
    return wynik

def z24(napisy):
    suma = sum(dekoduj(s) for s in napisy)
    return suma, koduj(suma)""",
"""assert z24(napisy_p) == (4841542, "+oooo****+oo+o+")
assert koduj(0) == "o"
""",
'Zakodowana suma może mieć więcej niż 12 znaków.'),
E('Jeden interfejs raportu',
"Napisz rozwiaz(napisy), zwracającą słownik '2.1'–'2.4'. Sprawdź wszystkie odpowiedzi przykładowe naraz.",
"""def rozwiaz(napisy):
    return {'2.1':z21(napisy), '2.2':z22(napisy), '2.3':z23(napisy), '2.4':z24(napisy)}""",
'assert rozwiaz(napisy_p) == {"2.1":["oooo+**+oooo"], "2.2":[(6,3)], "2.3":(519789,"***+o*ooo++o"), "2.4":(4841542,"+oooo****+oo+o+")}',
'Nie kopiuj ponownie kodu czterech algorytmów; wywołaj funkcje.'),
E('Pełne dane',
'Odczytaj symbole.txt, sprawdź 2000 napisów i zapisz raport w odp. Wyświetl go po przejściu wszystkich testów przykładu.',
"""napisy = wczytaj("symbole.txt")
assert len(napisy) == 2000
odp = rozwiaz(napisy)
print(odp)""",
"""assert len(odp["2.1"]) == 6
assert odp["2.2"] == [(399,5),(546,2),(630,11)]
assert odp["2.3"] == (531246,"*******o+*+o")
assert odp["2.4"] == (527865439,"++oo*+oo*++ooo*o*++")""",
'Nie wpisuj oczekiwanych odpowiedzi zamiast obliczeń.'),
E('wyniki2.txt',
'Sam otwórz wyniki2.txt do zapisu obok notatnika. Palindromy zapisz po jednym wierszu. Dla 2.2 podaj najpierw liczbę kwadratów, potem pary środków. Zapisz też maksimum i sumę w obu zapisach. Odczytaj plik do odczyt_wyniku i sprawdź zawartość.',
"""wiersze = ["2.1.", *odp["2.1"], f"2.2. {len(odp['2.2'])}"]
wiersze += [f"{r} {c}" for r, c in odp["2.2"]]
wiersze += [f"2.3. {odp['2.3'][0]} {odp['2.3'][1]}",
            f"2.4. {odp['2.4'][0]} {odp['2.4'][1]}"]
tekst = "\\n".join(wiersze) + "\\n"
with open("wyniki2.txt", "w", encoding="utf-8") as plik:
    plik.write(tekst)
with open("wyniki2.txt", "r", encoding="utf-8") as plik:
    odczyt_wyniku = plik.read()
print(odczyt_wyniku)""",
"""assert odczyt_wyniku == tekst
assert "2.4. 527865439 ++oo*+oo*++ooo*o*++" in odczyt_wyniku""",
'Numer części oddziela znaczenie kolejnych wierszy.'),
E('Samodzielnie: niezależne dekodowanie',
'Napisz dekoduj_test(s) przez str.translate i int(zapis,3). Porównaj z Hornerem dla wszystkich pełnych danych.',
"""def dekoduj_test(s):
    return int(s.translate(str.maketrans("o+*", "012")), 3)""",
'assert all(dekoduj(s) == dekoduj_test(s) for s in napisy)',
'To alternatywna implementacja testowa tej samej wartości.'),
E('Samodzielnie: plansza samych zer',
'Przygotuj planszę z pięciu wierszy po pięć znaków o. Ile bloków 3×3 zawiera? Zapisz wynik w srodki_test. Sprawdź pierwszy i ostatni środek.',
'srodki_test = z22(["o"*5 for _ in range(5)])',
"""assert len(srodki_test) == 9
assert srodki_test[0] == (2,2)
assert srodki_test[-1] == (4,4)""",
'Liczba bloków wynosi (h-2)*(w-2).'),
], official='2025_zadanie_2.md'),
lesson(11, 'nwd_ruch_i_geometria', 'Wektory, punkty i geometria całkowitoliczbowa',
'Przygotowanie całego algorytmu do zadania Dron z matury 2025.',
['Czy (dx,dy) jest położeniem czy zmianą położenia?', 'Czy punkt o współrzędnej x=5000 leży wewnątrz kwadratu 0<x<5000?', 'Jak sprawdzić środek odcinka bez dzielenia rzeczywistego?'],
[
T(1, 'Przesunięcie i położenie',
"""Punkt (x,y) opisuje położenie, a wektor (dx,dy) zmianę. Kolejny punkt powstaje przez (x+dx,y+dy). Sumowanie obu kolumn daje końcowe położenie, lecz do analizy drogi trzeba zapamiętać każdy punkt po ruchu.

W zadaniu Dron rozpatrujemy punkty po kolejnych ruchach, bez dodatkowego punktu startowego. Dodatnie dx oznacza, że współrzędna x rośnie ściśle, więc punkty są różne i uporządkowane od lewej do prawej.""",
"""x = y = 0
for dx,dy in [(3,2),(2,4),(5,-6)]:
    x += dx
    y += dy
    print(x,y)
assert (x,y) == (10,0)"""),
T(3, 'Wnętrze, brzeg i NWD',
"""Wnętrze kwadratu sprawdzamy ostrymi nierównościami. Użycie <= włącza brzeg, co zmienia treść zadania. Testy muszą obejmować każdy bok i narożniki.

NWD przesunięć liczymy dla wartości bezwzględnych: ruch w dół ma ujemne dy. NWD(A,0)=A dla A>0. Nie myl liczby ruchów spełniających warunek NWD z liczbą punktów leżących wewnątrz obszaru.""",
"""punkty = [(1,1),(0,1),(5000,1),(1,5000)]
for x,y in punkty:
    print((x,y), 0 < x < 5000 and 0 < y < 5000)"""),
T(6, 'Środek odcinka i koszt wyszukiwania',
"""M jest środkiem AC dokładnie wtedy, gdy 2*Mx=Ax+Cx i 2*My=Ay+Cy. Dzielenie całkowite bez sprawdzenia parzystości mogłoby zaokrąglić niecałkowity środek do istniejącego punktu.

Prosty algorytm sprawdza trójki w O(n³). Dla 100 punktów jest wykonalny, ale zbiór punktów pozwala sprawdzać środek każdej pary w średnim O(1), czyli łącznie oczekiwanym O(n²). Końce wybieraj jako i<j, sprawdzaj dwie parzystości i różność trzech punktów.""",
"""a, m, c = (2,2), (4,4), (6,6)
assert 2*m[0] == a[0]+c[0] and 2*m[1] == a[1]+c[1]
print("Środek potwierdzony")
print((0+3)//2)  # 1 nie jest dokładną połową 3"""),
],
[
E('Jeden ruch',
'Napisz przesun(punkt,ruch), zwracającą nowy punkt. Dla (3,2) i (2,-5): (5,-3).',
"""def przesun(punkt, ruch):
    return punkt[0]+ruch[0], punkt[1]+ruch[1]""",
'assert przesun((3,2),(2,-5)) == (5,-3)',
'Dodaj odpowiadające sobie współrzędne.'),
E('Cała trasa',
'Napisz trasa(ruchy) zwracającą punkty po ruchach od startu (0,0). Nie dodawaj startu do listy. Puste dane dają [].',
"""def trasa(ruchy):
    punkt = (0,0)
    wynik = []
    for ruch in ruchy:
        punkt = przesun(punkt, ruch)
        wynik.append(punkt)
    return wynik""",
"""assert trasa([(3,2),(2,4),(5,-6)]) == [(3,2),(5,6),(10,0)]
assert trasa([]) == []""",
'Każdy krok zaczyna się w końcu poprzedniego.'),
E('Ścisłe wnętrze',
'Napisz wewnatrz(punkt,bok=5000), sprawdzającą 0<x<bok i 0<y<bok. Dodaj testy punktów na wszystkich czterech krawędziach.',
"""def wewnatrz(punkt, bok=5000):
    x,y = punkt
    return 0 < x < bok and 0 < y < bok""",
"""assert wewnatrz((1,1))
assert all(not wewnatrz(p) for p in [(0,1),(5000,1),(1,0),(1,5000)])""",
'Brzeg nie jest wnętrzem.'),
E('NWD dla ruchu w dół',
'Napisz nwd(a,b) oraz ile_nwd(ruchy), zliczającą pary z NWD>1. Dla [(12,-18),(7,0),(5,3)] wynik to 2.',
"""def nwd(a, b):
    a,b = abs(a), abs(b)
    while b:
        a,b = b,a%b
    return a

def ile_nwd(ruchy):
    return sum(nwd(dx,dy) > 1 for dx,dy in ruchy)""",
"""assert ile_nwd([(12,-18),(7,0),(5,3)]) == 2
assert nwd(8,0) == 8""",
'Zero w drugiej współrzędnej nie oznacza automatycznie NWD=0.'),
E('Sprawdzenie trójki',
'Napisz jest_srodkiem(a,m,c), wymagającą trzech różnych punktów i dokładnej relacji środka. Dla (0,0),(1,1),(3,3) wynik musi być False.',
"""def jest_srodkiem(a,m,c):
    return (a != m and m != c and a != c and
            2*m[0] == a[0]+c[0] and 2*m[1] == a[1]+c[1])""",
"""assert jest_srodkiem((2,2),(4,4),(6,6))
assert not jest_srodkiem((0,0),(1,1),(3,3))
assert not jest_srodkiem((1,1),(1,1),(1,1))""",
'Unikaj zaokrąglania połowy nieparzystej sumy.'),
E('Dokładny kandydat na środek',
'Napisz srodek_calkowity(a,c), zwracającą krotkę, jeśli obie współrzędne środka są całkowite, albo None.',
"""def srodek_calkowity(a,c):
    sx,sy = a[0]+c[0], a[1]+c[1]
    if sx%2 or sy%2:
        return None
    return sx//2, sy//2""",
"""assert srodek_calkowity((2,2),(6,6)) == (4,4)
assert srodek_calkowity((0,0),(2,3)) is None""",
'Sprawdź parzystość obu sum przed //2.'),
E('Wyszukiwanie par i zbiór',
'Napisz trojki(punkty) dla różnych punktów o rosnącym x. Zwróć wszystkie (A,M,C), nie kończąc po pierwszym wyniku. Sprawdź także punkty niebędące sąsiednimi na liście.',
"""def trojki(punkty):
    dostepne = set(punkty)
    wynik = []
    for i,a in enumerate(punkty):
        for c in punkty[i+1:]:
            m = srodek_calkowity(a,c)
            if m in dostepne and jest_srodkiem(a,m,c):
                wynik.append((a,m,c))
    return wynik""",
"""assert trojki([(2,2),(3,8),(4,4),(6,6)]) == [((2,2),(4,4),(6,6))]
assert trojki([(0,0),(1,1),(3,3)]) == []""",
'Sprawdzenie wszystkich wyników pozwala zweryfikować gwarancję unikalności.'),
E('Raport trasy',
"""Napisz raport(ruchy,bok), zwracającą (liczba par z NWD>1, liczba punktów wewnątrz, trójki). Dla trzech ruchów (2,2) i boku 10 wynik to (3,3,[((2,2),(4,4),(6,6))]).

Sam otwórz ruchy-trening.txt i wczytaj pary przesunięć do ruchy_z_pliku. Oblicz raport_z_pliku dla boku 10 i zapisz trzy części raportu w trzech wierszach wyniki-trening.txt. Plik zawiera przesunięcia, nie gotowe punkty.""",
"""def raport(ruchy, bok):
    punkty = trasa(ruchy)
    return ile_nwd(ruchy), sum(wewnatrz(p,bok) for p in punkty), trojki(punkty)

ruchy_z_pliku = []
with open("ruchy-trening.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        dx, dy = [int(x) for x in wiersz.split()]
        ruchy_z_pliku.append((dx, dy))
raport_z_pliku = raport(ruchy_z_pliku, 10)
with open("wyniki-trening.txt", "w", encoding="utf-8") as plik:
    for czesc in raport_z_pliku:
        print(czesc, file=plik)""",
"""assert raport([(2,2)]*3,10) == (3,3,[((2,2),(4,4),(6,6))])
assert raport_z_pliku == (3, 3, [((2, 2), (4, 4), (6, 6))])""",
'Nie pomyl listy ruchów z listą punktów.'),
E('Samodzielnie: odległość od startu',
'Napisz najdalszy(punkty), zwracającą pierwszy punkt najdalszy od (0,0). Porównuj kwadraty odległości, bez pierwiastków. Załóż niepustą listę.',
"""def najdalszy(punkty):
    return max(punkty, key=lambda p: p[0]*p[0]+p[1]*p[1])""",
'assert najdalszy([(1,1),(3,4),(0,5)]) == (3,4)',
'Pierwiastek zachowuje porządek, więc nie trzeba go obliczać.'),
E('Samodzielnie: odtwórz ruchy',
'Napisz ruchy_z_punktow(punkty), odtwarzającą przesunięcia od startu (0,0). Sprawdź, czy odwrotna operacja odtwarza wejście.',
"""def ruchy_z_punktow(punkty):
    poprzedni = (0,0)
    wynik = []
    for x,y in punkty:
        wynik.append((x-poprzedni[0],y-poprzedni[1]))
        poprzedni = (x,y)
    return wynik""",
"""ruchy = [(3,2),(2,4),(5,-6)]
assert ruchy_z_punktow(trasa(ruchy)) == ruchy""",
'Odejmij poprzednie położenie od bieżącego.'),
], official=None),
lesson(12, 'matura_2025_zadanie_3_dron', 'Matura 2025: Dron i kompletne rozwiązanie',
'Pełne rozwiązanie zadania 3.1 i 3.2 a–b oraz samodzielne sprawdzenie całego procesu.',
['Dlaczego nie należy dodawać (0,0) do punktów rozpatrywanych w 3.2?', 'Jakie błędy wykrywa punkt na krawędzi?', 'Dlaczego należy sprawdzić unikalność znalezionej trójki?'],
[
T(1, 'Przekład polecenia na interfejsy',
"""Potrzebne są cztery niezależne funkcje: odczyt par, liczenie NWD, odtwarzanie punktów i wyszukiwanie geometryczne. Listy ruchów i punktów mają taką samą długość, ale przechowują inne dane.

Pełne dane mają 100 wierszy, przykładowe 10. Start to (0,0), końcowy punkt (20000,0). Warto sprawdzić te warunki jeszcze przed analizą szczegółowych odpowiedzi.""",
"""ruchy_demo = [(2000,1001),(2000,1004)]
x = sum(dx for dx,dy in ruchy_demo)
y = sum(dy for dx,dy in ruchy_demo)
assert (x,y) == (4000,2005)
print(x,y)"""),
T(3, 'Punkty po ruchach i warunki brzegowe',
"""Dla 3.2 a liczymy tylko punkty po ruchach, które spełniają oba ścisłe warunki 0<x<5000 i 0<y<5000. Dla 3.2 b punkty nie muszą być kolejne.

Współrzędne x rosną, więc przy i<j końce odcinka są różne. Środek leży pomiędzy nimi w osi x. Test parzystości chroni przed wskazaniem fałszywego środka przez dzielenie całkowite.""",
"""a,c = (0,0),(3,3)
print("Suma współrzędnych:", a[0]+c[0], a[1]+c[1])
assert (a[0]+c[0]) % 2 == 1"""),
T(6, 'Złożenie, plik i obrona rozwiązania',
"""Wynik 3.1 jest liczbą, 3.2 a także liczbą, a 3.2 b trójką punktów. Zachowaj te typy do etapu formatowania. W raporcie tekstowym podpisz 3.1 oraz obie części 3.2.

Na koniec uruchom rozwiązanie w świeżym jądrze, sprawdź przykład CKE, pełne dane i ponownie odczytaj plik. Przy odpowiedzi ustnej wyjaśnij, dlaczego trójka jest poprawna i jaki koszt ma wyszukiwanie.""",
"""a,m,c = (14000,3014),(16000,2010),(18000,1006)
assert 2*m[0] == a[0]+c[0]
assert 2*m[1] == a[1]+c[1]
print("Obie współrzędne spełniają relację środka.")"""),
],
[
E('Odczyt i warunki danych',
'Napisz wczytaj(nazwa): sam otwórz dron_przyklad.txt i wczytaj pary do ruchy_p. W każdym wierszu wymagaj dwóch liczb i dodatniego dx. Sprawdź 10 rekordów. Nie korzystaj z danych przygotowanych w innej karcie.',
"""def wczytaj(nazwa):
    ruchy = []
    with open(nazwa, "r", encoding="utf-8") as plik:
        for wiersz in plik:
            pola = wiersz.split()
            assert len(pola) == 2
            dx, dy = [int(pole) for pole in pola]
            assert dx > 0
            ruchy.append((dx, dy))
    return ruchy
ruchy_p = wczytaj("dron_przyklad.txt")""",
"""assert len(ruchy_p) == 10
assert ruchy_p[0] == (2000,1001)
assert ruchy_p[-1] == (2000,-1006)""",
'Waliduj rekord, zanim rozpakujesz dwa pola.'),
E('3.1: NWD i zliczanie',
'Napisz nwd(a,b) i z31(ruchy), zliczającą przesunięcia z NWD wartości bezwzględnych >1. Przykład CKE: 6.',
"""def nwd(a,b):
    a,b = abs(a),abs(b)
    while b:
        a,b = b,a%b
    return a

def z31(ruchy):
    return sum(nwd(dx,dy) > 1 for dx,dy in ruchy)""",
"""assert z31(ruchy_p) == 6
assert nwd(8,0) == 8
assert nwd(12,-18) == 6""",
'Przed pętlą Euklidesa normalizuj znaki.'),
E('Punkty po kolejnych ruchach',
'Napisz trasa(ruchy), bez dodatkowego punktu startowego. Potwierdź dwa pierwsze punkty przykładu i koniec (20000,0).',
"""def trasa(ruchy):
    x = y = 0
    wynik = []
    for dx,dy in ruchy:
        x += dx
        y += dy
        wynik.append((x,y))
    return wynik""",
"""punkty_p = trasa(ruchy_p)
assert punkty_p[:2] == [(2000,1001),(4000,2005)]
assert len(punkty_p) == 10
assert punkty_p[-1] == (20000,0)""",
'Dopisz punkt po aktualizacji obu współrzędnych.'),
E('3.2 a: wnętrze kwadratu',
'Napisz z32a(punkty). Dla przykładu ma zwrócić 2. Testami wyklucz wszystkie krawędzie.',
"""def z32a(punkty):
    return sum(0 < x < 5000 and 0 < y < 5000 for x,y in punkty)""",
"""assert z32a(punkty_p) == 2
assert z32a([(0,1),(5000,1),(1,0),(1,5000)]) == 0""",
'Użycie <= zmieniłoby odpowiedź.'),
E('3.2 b: wszystkie kandydatury',
'Napisz z32b(punkty), zwracającą listę trójek (A,M,C) dla końców uporządkowanych po x. Potwierdź dokładnie jedną trójkę w przykładzie.',
"""def z32b(punkty):
    dostepne = set(punkty)
    wynik = []
    for i,a in enumerate(punkty):
        for c in punkty[i+1:]:
            sx,sy = a[0]+c[0],a[1]+c[1]
            if sx%2 == 0 and sy%2 == 0:
                m = (sx//2,sy//2)
                if m in dostepne and m != a and m != c:
                    wynik.append((a,m,c))
    return wynik""",
"""assert z32b(punkty_p) == [((14000,3014),(16000,2010),(18000,1006))]
assert z32b([(0,0),(1,1),(3,3)]) == []""",
'Nie kończ przed sprawdzeniem, że rozwiązań jest dokładnie tyle, ile gwarantuje treść.'),
E('Całe zadanie na przykładzie',
'Napisz rozwiaz(ruchy), zwracającą (wynik 3.1, wynik 3.2 a, jedyna trójka). Sprawdź jedyność trójki i końcowy punkt trasy.',
"""def rozwiaz(ruchy):
    punkty = trasa(ruchy)
    assert punkty[-1] == (20000,0)
    trojki = z32b(punkty)
    assert len(trojki) == 1
    return z31(ruchy),z32a(punkty),trojki[0]""",
'assert rozwiaz(ruchy_p) == (6,2,((14000,3014),(16000,2010),(18000,1006)))',
'Rozróżnij listę możliwych rozwiązań i jedną trójkę do oddania.'),
E('Pełne dane i kontrola relacji',
'Wczytaj dron.txt, potwierdź 100 ruchów, uruchom rozwiaz i zapisz w odp. Niezależnie sprawdź obie równości dla zwróconej trójki.',
"""ruchy = wczytaj("dron.txt")
assert len(ruchy) == 100
odp = rozwiaz(ruchy)
a,m,c = odp[2]
assert 2*m[0] == a[0]+c[0] and 2*m[1] == a[1]+c[1]
print(odp)""",
'assert odp == (40,24,((5832,1801),(7410,1990),(8988,2179)))',
'Znalezione punkty muszą pochodzić z trasy, a nie z listy przesunięć.'),
E('wyniki3.txt i komplet oddania',
'Sam zapisz wyniki3.txt obok notatnika. Podpisz odpowiedzi 3.1, 3.2 a i 3.2 b. Odczytaj plik ponownie do odczyt_wyniku. Uruchom własny notatnik od początku i omów koszt O(n²) wyszukiwania.',
"""punkty_tekst = ", ".join(f"({x}, {y})" for x, y in odp[2])
tekst = f"3.1. {odp[0]}\\n3.2. a) {odp[1]}\\n3.2. b) {punkty_tekst}\\n"
with open("wyniki3.txt", "w", encoding="utf-8") as plik:
    plik.write(tekst)
with open("wyniki3.txt", "r", encoding="utf-8") as plik:
    odczyt_wyniku = plik.read()
print(odczyt_wyniku)""",
"""assert odczyt_wyniku == tekst
assert "3.1. 40" in odczyt_wyniku and "3.2. a) 24" in odczyt_wyniku""",
'Zachowaj kolejność A,M,C, żeby łatwo zweryfikować środek.'),
E('Samodzielnie: kontrola sześcienna',
'Napisz trojki_wolno(punkty), sprawdzającą wszystkie i<j<k. Dla rosnącego x środkowym punktem może być tylko j. Porównaj z z32b na przykładzie i pełnych danych.',
"""def trojki_wolno(punkty):
    wynik = []
    for i in range(len(punkty)):
        for j in range(i+1,len(punkty)):
            for k in range(j+1,len(punkty)):
                a,m,c = punkty[i],punkty[j],punkty[k]
                if 2*m[0] == a[0]+c[0] and 2*m[1] == a[1]+c[1]:
                    wynik.append((a,m,c))
    return wynik""",
"""assert trojki_wolno(punkty_p) == z32b(punkty_p)
assert trojki_wolno(trasa(ruchy)) == z32b(trasa(ruchy))""",
'Wolny algorytm jest dobrym wzorcem kontrolnym dla małego zbioru.'),
E('Samodzielnie: poprawność fizyczna trasy',
'Napisz poprawny_lot(ruchy), sprawdzającą dodatnie dx, końcowy punkt (20000,0) i dodatnią wysokość wszystkich punktów poza lądowaniem. Puste dane dają False.',
"""def poprawny_lot(ruchy):
    if not ruchy or any(dx <= 0 for dx,dy in ruchy):
        return False
    punkty = trasa(ruchy)
    return punkty[-1] == (20000,0) and all(y > 0 for x,y in punkty[:-1])""",
"""assert poprawny_lot(ruchy_p)
assert poprawny_lot(ruchy)
assert not poprawny_lot([(10000,0),(10000,0)])""",
'Warunek dotyczy też danych wejściowych, nie tylko wyniku zadania.'),
], official='2025_zadanie_3.md')
]
