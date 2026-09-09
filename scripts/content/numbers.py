from .common import lesson, theory as T, task as E

LESSONS = [
lesson(5, 'matura_2024_zadanie_3_nieparzysty_skrot', 'Matura 2024: Nieparzysty skrót krok po kroku',
'Pełne rozwiązanie zadania 3.1–3.3 z arkusza MINP-R0-100-2405.',
['Jaki warunek w pętli zachowuje tylko cyfry nieparzyste?', 'Dlaczego 0 może sygnalizować nieistniejący skrót?', 'Jakie operacje są dozwolone w funkcji wymaganej w 3.1?'],
[
T(1, 'Od specyfikacji do testów',
"""Przeczytaj oryginalne polecenia. Zadanie 3.1 wymaga algorytmu do zapisania w arkuszu: operacje wewnątrz funkcji muszą być całkowitoliczbowe. W 3.2 i 3.3 potrzebujemy także czytania plików i zapisania wyników.

Zbuduj funkcję zwracającą 0, jeśli wszystkie cyfry są parzyste. To rozszerzenie dziedziny pomocne w 3.2. Dla danych dopuszczonych w 3.1 nigdy nie zwróci zera. Nie zmieniaj kolejności cyfr i nie używaj str do implementacji skrótu.""",
"""n = 39101
wynik = 0
pozycja = 1
while n > 0:
    cyfra = n % 10
    n //= 10
    if cyfra % 2 != 0:
        wynik += cyfra * pozycja
        pozycja *= 10
print(wynik)
assert wynik == 3911"""),
T(3, 'Licznik i maksimum spełniających warunek',
"""Nie szukamy największej liczby w całym pliku, lecz największej w grupie bez skrótu. Najpierw filtr albo warunek w pętli, dopiero potem aktualizacja maksimum.

Polecenie gwarantuje co najmniej jeden taki rekord. Funkcję pomocniczą warto mimo to umieć przetestować na pustej grupie, zwracając (0,None). W pliku wynikowym dla danych maturalnych None nie powinno wystąpić.""",
"""liczby = [266, 97, 2428]
kandydaci = [266, 2428]
print(len(kandydaci), max(kandydaci))
print("Liczba rekordów:", len(liczby))"""),
T(6, 'Składanie podpunktów i dowody poprawności',
"""W 3.3 porównujemy NWD do 7, nie sprawdzamy tylko podzielności obu liczb przez 7: ich NWD może być większy. Każdy rekord rozpatrujemy niezależnie.

Testy przykładowe sprawdzają cały proces odczytu i obliczeń. Pełne pliki zawierają po 200 rekordów. Właściwe nazwy wyników to wyniki3_2.txt i wyniki3_3.txt. Pliki odpowiedzi zapisuj obok notatnika tej lekcji; nie mieszaj plików z różnych spotkań.""",
"""def nwd_demo(a, b):
    while b:
        a, b = b, a % b
    return a

print(nwd_demo(21, 63))  # obie podzielne przez 7, ale NWD to 21
assert nwd_demo(21, 63) != 7"""),
],
[
E('3.1: funkcja zgodna z ograniczeniami',
'Napisz skrot(n) arytmetycznie dla n>0. Zwracaj 0 przy braku skrótu. Przepisz funkcję tak, żeby można było zapisać ją na kartce bez biblioteki standardowej.',
"""def skrot(n):
    wynik = 0
    pozycja = 1
    while n > 0:
        c = n % 10
        n //= 10
        if c % 2 != 0:
            wynik += c * pozycja
            pozycja *= 10
    return wynik""",
"""assert skrot(294762) == 97
assert skrot(39101) == 3911
assert skrot(224) == 0""",
'Każda używana zmienna wewnątrz funkcji przechowuje liczbę całkowitą.'),
E('3.1: przypadki brzegowe',
'Zbuduj testy dla cyfr 1,2,9 oraz liczb 10101,20003,86420. Zapisz wyniki w slownik_testow. Wyjaśnij, dlaczego zera znikają.',
'slownik_testow = {n: skrot(n) for n in [1, 2, 9, 10101, 20003, 86420]}',
'assert slownik_testow == {1: 1, 2: 0, 9: 9, 10101: 111, 20003: 3, 86420: 0}',
'Zero jest cyfrą parzystą.'),
E('Wczytanie obu przykładów',
'Napisz wczytaj(nazwa): sam otwórz plik, wczytaj każdą liczbę i zwróć listę. Wczytaj skrot_przyklad.txt do przyklad_1 oraz skrot2_przyklad.txt do przyklad_2. Oba pliki leżą obok notatnika. Potwierdź po 20 rekordów.',
"""def wczytaj(nazwa):
    liczby = []
    with open(nazwa, "r", encoding="utf-8") as plik:
        for wiersz in plik:
            liczby.append(int(wiersz))
    return liczby
przyklad_1 = wczytaj("skrot_przyklad.txt")
przyklad_2 = wczytaj("skrot2_przyklad.txt")""",
"""assert len(przyklad_1) == len(przyklad_2) == 20
assert all(0 < n < 30000 for n in przyklad_1 + przyklad_2)""",
'Nazwy skrot i skrot2 dotyczą innych podpunktów.'),
E('3.2: liczność i największy element',
'Napisz bez_skrotu(liczby), zwracającą (liczba rekordów bez skrótu, maksimum). Gdy grupa jest pusta, zwróć (0,None). Potwierdź (2,2428) dla pierwszego przykładu.',
"""def bez_skrotu(liczby):
    ile = 0
    najwieksza = None
    for n in liczby:
        if skrot(n) == 0:
            ile += 1
            if najwieksza is None or n > najwieksza:
                najwieksza = n
    return ile, najwieksza""",
"""assert bez_skrotu(przyklad_1) == (2, 2428)
assert bez_skrotu([135, 97]) == (0, None)""",
'Aktualizacja maksimum musi być wewnątrz warunku brakującego skrótu.'),
E('3.3: funkcja NWD',
'Napisz nwd(a,b) dla nieujemnych argumentów. Potwierdź, że NWD liczby 4872 i jej skrótu wynosi 7.',
"""def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a""",
"""assert skrot(4872) == 7
assert nwd(4872, skrot(4872)) == 7
assert nwd(21, 63) == 21""",
'Warunek maturalny dotyczy największego dzielnika.'),
E('3.3: lista odpowiedzi',
'Napisz nwd_siedem(liczby). Zachowaj kolejność oraz wszystkie wystąpienia, nie używaj set. Sprawdź przykład CKE.',
"""def nwd_siedem(liczby):
    wynik = []
    for n in liczby:
        m = skrot(n)
        if m != 0 and nwd(n, m) == 7:
            wynik.append(n)
    return wynik""",
"""assert nwd_siedem(przyklad_2) == [4872, 23527]
assert nwd_siedem([4872, 4872]) == [4872, 4872]""",
'Lista wynikowa nie wymaga sortowania.'),
E('Obliczenia na pełnych danych',
'Wczytaj skrot.txt i skrot2.txt. Sprawdź liczbę rekordów. Zapisz odpowiedzi w odp_32 i odp_33. Przed odczytaniem klucza na końcu karty wyjaśnij każdy wynik.',
"""pelne_1 = wczytaj('skrot.txt')
pelne_2 = wczytaj('skrot2.txt')
assert len(pelne_1) == len(pelne_2) == 200
odp_32 = bez_skrotu(pelne_1)
odp_33 = nwd_siedem(pelne_2)
print('3.2:', odp_32)
print('3.3:', odp_33)""",
"""assert odp_32 == (18, 28422)
assert odp_33 == [784, 14196, 2247, 24087, 3871, 10192]""",
'Ostateczny przebieg musi korzystać z nazw bez dopisku przyklad.'),
E('Pliki odpowiedzi i kontrola po zapisie',
'Sam otwórz pliki wynikowe do zapisu. Zapisz odp_32 jako dwa wiersze do wyniki3_2.txt i odp_33 po jednej liczbie do wyniki3_3.txt. Pliki mają powstać obok notatnika. Wczytaj je ponownie własną funkcją i porównaj z obliczeniami.',
"""p32 = "wyniki3_2.txt"
p33 = "wyniki3_3.txt"
with open(p32, "w", encoding="utf-8") as plik:
    print(odp_32[0], file=plik)
    print(odp_32[1], file=plik)
with open(p33, "w", encoding="utf-8") as plik:
    for n in odp_33:
        print(n, file=plik)""",
"""assert tuple(wczytaj(p32)) == odp_32
assert wczytaj(p33) == odp_33""",
'Sprawdzaj plik, który oddajesz, nie tylko wcześniejszy print.'),
E('Samodzielnie: niezależny wzorzec testowy',
'Napisz skrot_testowy(n) używając str. Porównaj oba algorytmy dla 1–999. Ta wersja jest wyłącznie narzędziem testowym; do 3.1 oddajesz funkcję arytmetyczną.',
"""def skrot_testowy(n):
    zapis = "".join(c for c in str(n) if int(c) % 2 == 1)
    return int(zapis) if zapis else 0""",
"""for n in range(1, 1000):
    assert skrot(n) == skrot_testowy(n)""",
'Inna implementacja pomaga wykryć błędną kolejność cyfr.'),
E('Samodzielnie: własność skrótu',
'Sprawdź dla n=1–999, że ponowne obliczenie istniejącego skrótu go nie zmienia. Zapisz wynik wszystkich porównań w idempotentny i uzasadnij tę własność.',
'idempotentny = all(skrot(skrot(n)) == skrot(n) for n in range(1, 1000) if skrot(n) != 0)',
'assert idempotentny',
'W istniejącym skrócie nie pozostała już żadna parzysta cyfra.'),
], official='2024_zadanie_3.md'),
lesson(6, 'sortowanie_zliczanie_i_czynniki', 'Sortowanie, liczności i rozkład na czynniki',
'Przygotowanie do podpunktów 4.1–4.3 matury 2024.',
['Czy sto pierwsza liczba po sortowaniu ma indeks 100 czy 101?', 'Czym zbiór {2,3} różni się od listy [2,2,3]?', 'Kiedy wystarczy znaleźć jeden pasujący dzielnik?'],
[
T(1, 'Sortowanie z zachowaniem wystąpień',
"""sorted tworzy nową uporządkowaną listę, a lista.sort zmienia obecną listę i zwraca None. reverse=True oznacza porządek malejący. Pozycja k liczona od 1 ma indeks k-1.

Nie usuwaj duplikatów przed wyborem k-tego elementu, jeśli polecenie nie wymaga różnych wartości. W ciągu 4,4,3 druga największa liczba to 4, nie 3. Zachowaj oryginalną kolejność danych, jeśli później szukasz fragmentów ciągu.""",
"""a = [2, 4, 2, 3, 3, 4]
b = sorted(a, reverse=True)
print(a, b, b[1])
assert b[1] == 4"""),
T(3, 'Istnieje a dla każdego',
"""any(warunki) zwraca True, gdy choć jeden warunek jest prawdziwy; all wymaga wszystkich. Odpowiednikiem any jest pętla zakończona break po znalezieniu pierwszego dopasowania.

W zadaniu o dzielnikach każdy element pierwszego wiersza liczymy najwyżej raz, nawet jeśli dzieli pięć liczb z drugiego wiersza. Jednak dwa wystąpienia tego samego elementu w pierwszym wierszu liczymy oddzielnie.""",
"""pierwszy = [2, 2, 3, 7]
drugi = [12, 15]
wynik = sum(any(n % p == 0 for n in drugi) for p in pierwszy)
print(wynik)
assert wynik == 3"""),
T(6, 'Zapas czynników i niezależność prób',
"""Rozkład na czynniki pierwsze mówi, ile razy każda liczba pierwsza jest potrzebna. Counter(lista) buduje słownik dostępnych liczności. Można też przejść po całej liście czynników i dzielić pozostałą liczbę tylko raz na wystąpienie.

Gdy pozostało 1, liczba jest zbudowana. Gdy nie da się już dzielić i pozostało więcej niż 1, brakuje czynników. Każdą nową liczbę sprawdzamy z pełnym zapasem, bo zadanie nie wymaga jednoczesnego budowania wszystkich liczb.""",
"""from collections import Counter
dostepne = Counter([2, 2, 3, 5])
potrzebne = Counter([2, 2, 2, 2])
print(dostepne, potrzebne)
print(potrzebne[2] <= dostepne[2])"""),
],
[
E('Ranking z powtórzeniami',
'Napisz kta(liczby,k), zwracającą k-tą liczbę od największej. Załóż 1<=k<=len(liczby). Nie zmieniaj argumentu.',
"""def kta(liczby, k):
    return sorted(liczby, reverse=True)[k - 1]""",
"""a = [2, 4, 2, 3, 3, 4]
assert kta(a, 2) == 4
assert a == [2, 4, 2, 3, 3, 4]""",
'sorted nie usuwa powtórzeń.'),
E('Liczności bez biblioteki',
'Napisz licznik(dane) budującą słownik wystąpień. Sprawdź [2,2,3,5,3].',
"""def licznik(dane):
    wynik = {}
    for n in dane:
        wynik[n] = wynik.get(n, 0) + 1
    return wynik""",
'assert licznik([2, 2, 3, 5, 3]) == {2: 2, 3: 2, 5: 1}',
'Nowy klucz zaczyna od wartości 0.'),
E('Choć jedna wielokrotność',
'Napisz dzieli_jakas(p,liczby), kończącą szukanie po pierwszej wielokrotności p. Załóż p>0; pusta lista daje False.',
"""def dzieli_jakas(p, liczby):
    for n in liczby:
        if n % p == 0:
            return True
    return False""",
"""assert dzieli_jakas(3, [7, 12, 15])
assert not dzieli_jakas(7, [])""",
'False zwróć dopiero po sprawdzeniu całej listy.'),
E('Zliczanie wystąpień dzielników',
'Napisz licz_dzielniki(pierwszy,drugi). Dla [2,2,3,7] i [12,15] wynik to 3, a nie 2 ani 4.',
"""def licz_dzielniki(pierwszy, drugi):
    return sum(dzieli_jakas(p, drugi) for p in pierwszy)""",
'assert licz_dzielniki([2, 2, 3, 7], [12, 15]) == 3',
'Nie zliczaj par (p,n); zliczaj pasujące wystąpienia p.'),
E('Rozkład liczby',
'Napisz rozklad(n) dla n>=2, zwracającą listę czynników pierwszych od najmniejszego. Dla 72: [2,2,2,3,3]. Po pętli uwzględnij pozostały duży czynnik.',
"""def rozklad(n):
    wynik = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            wynik.append(d)
            n //= d
        d += 1
    if n > 1:
        wynik.append(n)
    return wynik""",
"""assert rozklad(72) == [2, 2, 2, 3, 3]
assert rozklad(17) == [17]""",
'Gdy d*d przekracza pozostałą liczbę, reszta >1 musi być pierwsza.'),
E('Ograniczony iloczyn',
'Napisz mozna(n,pierwsze), sprawdzającą budowę n z dostarczonych wystąpień liczb pierwszych. Dla [2,2,3,5]: 12 i 20 są możliwe, 16 nie.',
"""def mozna(n, pierwsze):
    pozostalo = n
    for p in pierwsze:
        if pozostalo % p == 0:
            pozostalo //= p
    return pozostalo == 1""",
"""assert mozna(12, [2, 2, 3, 5])
assert mozna(20, [2, 2, 3, 5])
assert not mozna(16, [2, 2, 3, 5])""",
'Jedno wystąpienie w liście daje prawo do jednego dzielenia.'),
E('Dlaczego while może być błędem',
'Napisz brakujace(n,pierwsze), zwracającą słownik brakujących czynników i liczności. Dla 16 i [2,2,3] wynik to {2:2}; dla 12 to {}.',
"""def brakujace(n, pierwsze):
    potrzeby = licznik(rozklad(n))
    zapas = licznik(pierwsze)
    return {p: ile - zapas.get(p, 0) for p, ile in potrzeby.items() if ile > zapas.get(p, 0)}""",
"""assert brakujace(16, [2, 2, 3]) == {2: 2}
assert brakujace(12, [2, 2, 3]) == {}""",
'Bez ograniczenia liczności while n%p==0 zużyłby czynnik dowolnie wiele razy.'),
E('Raport zbiorczy',
"""Napisz raport(pierwsze,liczby,k), zwracającą (liczba pasujących dzielników, k-ta największa, lista budowalnych liczb). Dla [2,2,3,5], [12,16,20], k=2: (4,3,[12,20]).

Teraz sam otwórz czynniki-trening.txt: pierwszy wiersz zawiera czynniki, drugi badane liczby. Wczytaj dwie listy i oblicz raport_z_pliku dla k=2. Zapisz trzy części raportu w trzech wierszach wyniki-trening.txt. Nie zastępuj odczytu wpisaniem list do kodu.""",
"""def raport(pierwsze, liczby, k):
    return (licz_dzielniki(pierwsze, liczby), kta(pierwsze, k),
            [n for n in liczby if mozna(n, pierwsze)])

with open("czynniki-trening.txt", "r", encoding="utf-8") as plik:
    wiersze = plik.read().splitlines()
pierwsze_z_pliku = [int(x) for x in wiersze[0].split()]
liczby_z_pliku = [int(x) for x in wiersze[1].split()]
raport_z_pliku = raport(pierwsze_z_pliku, liczby_z_pliku, 2)
with open("wyniki-trening.txt", "w", encoding="utf-8") as plik:
    print(raport_z_pliku[0], file=plik)
    print(raport_z_pliku[1], file=plik)
    print(*raport_z_pliku[2], file=plik)""",
"""assert raport([2, 2, 3, 5], [12, 16, 20], 2) == (4, 3, [12, 20])
assert raport_z_pliku == (4, 3, [12, 20])""",
'Każde wywołanie mozna rozpoczyna od całej badanej liczby.'),
E('Samodzielnie: druga różna',
'Napisz druga_rozna(liczby). Tym razem powtórzenia należy pominąć. Gdy różnych wartości jest mniej niż 2, zwróć None.',
"""def druga_rozna(liczby):
    rozne = sorted(set(liczby), reverse=True)
    return rozne[1] if len(rozne) > 1 else None""",
"""assert druga_rozna([7, 7, 3, 2]) == 3
assert druga_rozna([7, 7]) is None""",
'Zmieniony warunek zadania uzasadnia użycie set.'),
E('Samodzielnie: test dwóch algorytmów',
'Dla n=2–199 porównaj mozna z kontrolą brakujace(n,pierwsze)=={}. Użyj pierwsze=[2,2,3,5,7].',
"""pierwsze_test = [2, 2, 3, 5, 7]
zgodne = all(mozna(n, pierwsze_test) == (brakujace(n, pierwsze_test) == {}) for n in range(2, 200))""",
'assert zgodne',
'Rozkład i kolejne dzielenia są niezależnymi drogami do tej samej odpowiedzi.'),
], official=None),
lesson(7, 'sumy_prefiksowe_i_fragmenty', 'Sumy prefiksowe, okna i porównywanie średnich',
'Przygotowanie poprawnej i wystarczająco szybkiej analizy fragmentów w 4.4 matury 2024.',
['Czym spójny fragment różni się od dowolnie wybranego podciągu?', 'Ile jest fragmentów długości 3 w liście 7-elementowej?', 'Czy największa suma oznacza zawsze największą średnią?'],
[
T(1, 'Przedziały półotwarte',
"""Fragment a[l:r] zawiera indeks l, wyklucza r i ma r-l elementów. Fragment dochodzący do końca listy ma r=len(a). Spójność oznacza, że żadnego elementu między końcami nie wolno pominąć.

Wygodnie przyjąć jeden sposób zapisu końców w całym algorytmie. Prawy koniec wyłączny pasuje do range, wycinków i sum prefiksowych.""",
"""a = [3, 1, 8, 2, 7]
l, r = 1, 4
print(a[l:r], r-l, sum(a[l:r]))
assert a[l:r] == [1, 8, 2]"""),
T(3, 'Prefiksy i koszt obliczeń',
"""P[0]=0; P[i] to suma pierwszych i elementów. Dodawanie kolejnych elementów tworzy n+1 prefiksów. Suma a[l:r] to P[r]-P[l]. Liczymy ją w O(1), gdy prefiksy są gotowe.

Jest O(n²) par końców. Sumowanie każdego wycinka osobno daje O(n³), a sumy prefiksowe zmniejszają koszt do O(n²). Dla stałej długości k wystarczy n-k+1 okien, więc można przejść po nich w O(n).""",
"""a = [3, 1, 8, 2, 7]
p = [0]
for n in a:
    p.append(p[-1] + n)
assert p[4] - p[1] == 11
print(p)"""),
T(6, 'Średnia, minimum długości i remisy',
"""Suma 18 z 3 elementów daje średnią 6, a suma 17 z 2 elementów 8,5. Maksymalizacja sumy nie wystarczy. Dodatnie długości pozwalają porównać średnie dokładnie: s1*d2 > s2*d1.

Sprawdzaj wszystkie długości od minimum do końca danych, nie tylko minimum. Przechodź po początkach rosnąco i aktualizuj wynik tylko przy ścisłej poprawie. To zachowa najwcześniejszy początek. Gdy ten sam początek daje równe średnie przy różnych końcach, w kursie zachowujemy krótszy fragment.""",
"""s1, d1 = 18, 3
s2, d2 = 17, 2
print(s1 * d2 > s2 * d1)
assert s2 * d1 > s1 * d2"""),
],
[
E('Końce fragmentu',
'Napisz opis(a,l,r), zwracającą (fragment, długość, suma), przy 0<=l<=r<=len(a). Uwzględnij pusty fragment.',
"""def opis(a, l, r):
    return a[l:r], r-l, sum(a[l:r])""",
"""assert opis([3, 1, 8, 2], 1, 4) == ([1, 8, 2], 3, 11)
assert opis([3], 0, 0) == ([], 0, 0)""",
'r nie należy do fragmentu.'),
E('Ile okien?',
'Napisz liczba_okien(n,k) dla n>=0, k>=1. Gdy k>n, zwróć 0. Dla n=7,k=3 wynik to 5.',
"""def liczba_okien(n, k):
    return max(0, n-k+1)""",
"""assert liczba_okien(7, 3) == 5
assert liczba_okien(3, 3) == 1
assert liczba_okien(2, 3) == 0""",
'Pierwszy początek to 0, ostatni n-k.'),
E('Budowa prefiksów',
'Napisz prefiksy(a), zwracającą listę n+1 sum zaczynającą się od zera. Dla [3,1,8]: [0,3,4,12].',
"""def prefiksy(a):
    p = [0]
    for n in a:
        p.append(p[-1] + n)
    return p""",
"""assert prefiksy([3, 1, 8]) == [0, 3, 4, 12]
assert prefiksy([]) == [0]""",
'Zerowy prefiks umożliwia fragmenty zaczynające się od 0.'),
E('Odpowiadanie na zapytania',
'Napisz sumy_fragmentow(a,zapytania). Zbuduj prefiksy tylko raz, a następnie zwróć sumę dla każdej pary (l,r).',
"""def sumy_fragmentow(a, zapytania):
    p = prefiksy(a)
    return [p[r]-p[l] for l, r in zapytania]""",
'assert sumy_fragmentow([3, 1, 8, 2], [(0, 4), (1, 3), (2, 2)]) == [14, 9, 0]',
'Nie wywołuj prefiksy ponownie dla każdego pytania.'),
E('Najlepsze stałe okno',
'Napisz stale_okno(a,k), zwracającą (największa suma, pierwszy indeks początku) dla 1<=k<=len(a). Przy remisie pierwszy. Dla [1,8,9,2,10], k=2: (17,1).',
"""def stale_okno(a, k):
    p = prefiksy(a)
    najlepsza = None
    poczatek = 0
    for l in range(len(a)-k+1):
        suma = p[l+k]-p[l]
        if najlepsza is None or suma > najlepsza:
            najlepsza, poczatek = suma, l
    return najlepsza, poczatek""",
"""assert stale_okno([1, 8, 9, 2, 10], 2) == (17, 1)
assert stale_okno([-5, -2], 1) == (-2, 1)""",
'Inicjalizacja maksimum na 0 nie działa dla ujemnych sum.'),
E('Dokładne porównanie',
'Napisz lepsza(s1,d1,s2,d2), która sprawdza s1/d1 > s2/d2 bez dzielenia. Załóż dodatnie długości. Sprawdź też remis 10/2 i 15/3.',
"""def lepsza(s1, d1, s2, d2):
    return s1*d2 > s2*d1""",
"""assert lepsza(17, 2, 18, 3)
assert not lepsza(10, 2, 15, 3)""",
'Iloczyny krzyżowe zachowują dokładność int.'),
E('Wszystkie długości od minimum',
'Napisz najlepszy(a,k), zwracającą (suma, długość, początek), dla 1<=k<=len(a). Użyj prefiksów. Dla [9,1,9] i k=2 wygrywa cały fragment: (19,3,0).',
"""def najlepszy(a, k):
    assert 1 <= k <= len(a)
    p = prefiksy(a)
    best = None
    for l in range(len(a)-k+1):
        for r in range(l+k, len(a)+1):
            suma, dlugosc = p[r]-p[l], r-l
            if best is None or lepsza(suma, dlugosc, best[0], best[1]):
                best = (suma, dlugosc, l)
    return best""",
"""assert najlepszy([9, 1, 9], 2) == (19, 3, 0)
assert najlepszy([1, 8, 9, 2, 10], 2) == (17, 2, 1)""",
'Prawy koniec range musi dopuścić len(a).'),
E('Ostatni fragment i remis',
"""Zapisz testy najlepszy dla [0,0,9,9] z k=2, [5,5,5] z k=2 i [2,4] z k=2. Dla każdego uzasadnij, jaki błąd wykrywa.

Sam otwórz fragmenty-trening.txt i wczytaj liczby rozdzielone spacjami do ciag_z_pliku. Dla k=2 zapisz wynik_z_pliku oraz wyniki-trening.txt zawierający sumę, długość i indeks początku. Zachowaj kolejność pliku.""",
"""test_ostatni = najlepszy([0, 0, 9, 9], 2)
test_remis = najlepszy([5, 5, 5], 2)
test_calosc = najlepszy([2, 4], 2)

with open("fragmenty-trening.txt", "r", encoding="utf-8") as plik:
    ciag_z_pliku = [int(x) for x in plik.read().split()]
wynik_z_pliku = najlepszy(ciag_z_pliku, 2)
with open("wyniki-trening.txt", "w", encoding="utf-8") as plik:
    print(*wynik_z_pliku, file=plik)""",
"""assert test_ostatni == (18, 2, 2)
assert test_remis == (10, 2, 0)
assert test_calosc == (6, 2, 0)
assert wynik_z_pliku == (18, 2, 2)""",
'Sprawdź końce pętli i różnicę między > oraz >=.'),
E('Samodzielnie: okno przesuwne',
'Napisz stale_okno_bez_prefiksow(a,k). Przesuwając okno, odejmuj wychodzący element i dodawaj wchodzący. Porównaj z wcześniejszym algorytmem.',
"""def stale_okno_bez_prefiksow(a, k):
    suma = sum(a[:k])
    wynik = (suma, 0)
    for r in range(k, len(a)):
        suma += a[r] - a[r-k]
        if suma > wynik[0]:
            wynik = (suma, r-k+1)
    return wynik""",
'assert stale_okno_bez_prefiksow([1, 8, 9, 2, 10], 2) == stale_okno([1, 8, 9, 2, 10], 2)',
'Pamiętasz tylko sumę bieżącego okna, a nie wszystkie prefiksy.'),
E('Samodzielnie: sprawdzanie przez enumerację',
'Napisz wzorzec(a,k) używając sum(a[l:r]) i Fraction. Ma być prostym, wolnym wzorcem do testowania najlepszy na małych danych.',
"""from fractions import Fraction
def wzorzec(a, k):
    best = None
    for l in range(len(a)-k+1):
        for r in range(l+k, len(a)+1):
            kandydat = (sum(a[l:r]), r-l, l)
            if best is None or Fraction(kandydat[0], kandydat[1]) > Fraction(best[0], best[1]):
                best = kandydat
    return best""",
"""for a in [[9, 1, 9], [-3, -2, -4], [5, 5, 5], [0, 0, 9, 9]]:
    for k in range(1, len(a)+1):
        assert najlepszy(a, k) == wzorzec(a, k)""",
'Wzorzec ma być czytelny i niezależny od prefiksów, nie wydajny.'),
], official=None),
lesson(8, 'matura_2024_zadanie_4_liczby', 'Matura 2024: Liczby — cztery podpunkty',
'Pełne zadanie 4.1–4.4 z przykładami, obliczeniami i plikiem odpowiedzi.',
['Czy sortowanie może zniszczyć dane potrzebne do 4.4?', 'Czy dany czynnik wolno zużyć ponownie dla następnego kandydata?', 'Który fragment wygrywa przy równej średniej?'],
[
T(1, 'Jedno wejście, różne interpretacje',
"""Pierwszy wiersz służy jako lista wystąpień dzielników, lista do rankingu, zapas czynników i uporządkowany ciąg. W różnych podpunktach inne własności są ważne. Odczytaj dane raz i nie zmieniaj pierwszej listy przez sortowanie w miejscu.

Nie zakładaj 3000 elementów podczas odczytu przykładu: w nim jest 200 liczb. Sprawdź rozmiary po odczycie. Algorytmy powinny korzystać z długości listy.""",
"""lista = [5, 2, 3, 2]
ranking = sorted(lista, reverse=True)
print(lista, ranking)
assert lista == [5, 2, 3, 2]"""),
T(3, 'Dokładne odczytanie kwantyfikatorów',
"""W 4.1 pytanie brzmi, ile wystąpień z pierwszego wiersza dzieli jakąkolwiek liczbę z drugiego. W 4.3 sprawdzamy, czy wystąpienia czynników wystarczą dla każdego kandydata osobno.

W 4.2 sto pierwsza pozycja ma indeks 100. Dla 4.4 nie używaj posortowanej kopii: spójność dotyczy oryginalnego pliku.""",
"""a = [2, 2, 3]
b = [12, 18]
print(sum(any(n % p == 0 for n in b) for p in a))
print(sorted(a, reverse=True)[0])"""),
T(6, 'Cały proces i precyzja wyniku',
"""Średnie porównujemy przez iloczyny liczb całkowitych. Dopiero końcowy iloraz formatujemy do zapisu dziesiętnego. Zachowaj także dokładną sumę i długość; weryfikacja nie musi opierać się na zaokrągleniu.

Arkusz nie nakazuje w 4.4 dwóch miejsc po przecinku. Dla pełnych danych prezentujemy 10 miejsc oraz zapamiętujemy dokładną sumę i długość w kodzie. Każdą odpowiedź w wyniki4.txt poprzedź numerem podpunktu.""",
"""suma, dlugosc = 276, 50
print(f"{suma / dlugosc:.10f}".rstrip("0").rstrip("."))
assert suma / dlugosc == 5.52"""),
],
[
E('Odczyt i kontrola przykładów',
'Napisz wczytaj(nazwa): sam otwórz plik, odczytaj dwa wiersze i zamień je na dwie listy liczb. Wczytaj liczby_przyklad.txt do pa i pb. Sprawdź długości 200 i 20.',
"""def wczytaj(nazwa):
    with open(nazwa, "r", encoding="utf-8") as plik:
        wiersze = plik.read().splitlines()
    assert len(wiersze) == 2
    return [int(x) for x in wiersze[0].split()], [int(x) for x in wiersze[1].split()]
pa, pb = wczytaj("liczby_przyklad.txt")""",
'assert (len(pa), len(pb)) == (200, 20)',
'Każdy wiersz ma odrębne znaczenie.'),
E('4.1: wystąpienia dzielników',
'Napisz z41(a,b), zwracającą liczność zgodną z 4.1. Przykład CKE: 199.',
"""def z41(a, b):
    return sum(any(n % p == 0 for n in b) for p in a)""",
"""assert z41(pa, pb) == 199
assert z41([2, 2, 3, 7], [12, 15]) == 3""",
'any ogranicza zliczanie jednego wystąpienia do jednego trafienia.'),
E('4.2: sto pierwsza',
'Napisz z42(a). Zwróć element o indeksie 100 z nowej listy uporządkowanej malejąco. Przykład: 5.',
"""def z42(a):
    return sorted(a, reverse=True)[100]""",
"""kopia = pa.copy()
assert z42(pa) == 5
assert pa == kopia""",
'Nie zmieniaj a, bo będzie potrzebne do 4.4.'),
E('4.3: ograniczona liczność',
'Napisz z43(a,b), zwracającą budowalne liczby z b. Każde wystąpienie p w a daje jedno dzielenie. Przykład to [10,12,14,15,18,20,21,25,27,28].',
"""def z43(a, b):
    wynik = []
    for n in b:
        reszta = n
        for p in a:
            if reszta % p == 0:
                reszta //= p
        if reszta == 1:
            wynik.append(n)
    return wynik""",
"""assert z43(pa, pb) == [10, 12, 14, 15, 18, 20, 21, 25, 27, 28]
assert z43([2, 2, 3], [12, 12, 16]) == [12, 12]""",
'Resetuj reszta dla każdej liczby n.'),
E('4.4: prefiksy i wszystkie granice',
'Napisz z44(a,k=50), zwracającą (najlepsza suma,długość,indeks początku). Uwzględnij ostatni element i fragment długości dokładnie k.',
"""def z44(a, k=50):
    assert 1 <= k <= len(a)
    p = [0]
    for n in a:
        p.append(p[-1] + n)
    best = None
    for l in range(len(a)-k+1):
        for r in range(l+k, len(a)+1):
            s, d = p[r]-p[l], r-l
            if best is None or s*best[1] > best[0]*d:
                best = (s, d, l)
    return best""",
"""s, d, l = z44(pa)
assert (s, d, pa[l]) == (276, 50, 5)
assert z44([9, 1, 9], 2) == (19, 3, 0)""",
'Przy równości zachowaj dotychczasowy wynik.'),
E('Zintegrowane rozwiązanie',
'Napisz rozwiaz(a,b), zwracającą odpowiedzi czterech podpunktów w słowniku. W 4.4 zachowaj (suma,długość,pierwsza liczba). Zweryfikuj cały przykład jednym porównaniem.',
"""def rozwiaz(a, b):
    s, d, l = z44(a)
    return {'4.1': z41(a, b), '4.2': z42(a), '4.3': z43(a, b), '4.4': (s, d, a[l])}""",
"assert rozwiaz(pa, pb) == {'4.1': 199, '4.2': 5, '4.3': [10,12,14,15,18,20,21,25,27,28], '4.4': (276,50,5)}",
'W kodzie nie trać dokładnej sumy przez przedwczesne zaokrąglenie.'),
E('Przejście do pełnego pliku',
'Wczytaj liczby.txt, potwierdź 3000 i 20 liczb, wyznacz odpowiedzi w odp. Wypisz również dokładną sumę najlepszego fragmentu.',
"""a, b = wczytaj('liczby.txt')
assert (len(a), len(b)) == (3000, 20)
odp = rozwiaz(a, b)
print(odp)""",
"""assert odp['4.1'] == 212
assert odp['4.2'] == 1933
assert odp['4.3'] == [547839600, 2954285, 573219169, 573549984, 212444924]
assert odp['4.4'][1:] == (61, 1847)""",
'Przykład sprawdza format, lecz pełny plik może ujawnić inne błędy.'),
E('wyniki4.txt',
'Sam otwórz wyniki4.txt do zapisu obok notatnika. Zapisz cztery podpisane odpowiedzi. W 4.4 wypisz średnią do 10 miejsc, długość i pierwszą liczbę. Odczytaj plik ponownie do odczyt i sprawdź jego format.',
"""s, d, pierwszy = odp["4.4"]
plik_wyniku = "wyniki4.txt"
with open(plik_wyniku, "w", encoding="utf-8") as plik:
    print("4.1.", odp["4.1"], file=plik)
    print("4.2.", odp["4.2"], file=plik)
    print("4.3.", *odp["4.3"], file=plik)
    print(f"4.4. {s/d:.10f} {d} {pierwszy}", file=plik)
with open(plik_wyniku, "r", encoding="utf-8") as plik:
    odczyt = plik.read().splitlines()
print("\\n".join(odczyt))""",
"""assert len(odczyt) == 4
assert all(w.startswith(f'4.{i}. ') for i, w in enumerate(odczyt, 1))""",
'Zapisywanie odpowiedzi jest osobnym etapem, który też wymaga sprawdzenia.'),
E('Samodzielnie: test początku i końca',
'Napisz testy z44 dla [10,10,0,0], [0,0,10,10] oraz [5,5,5], zawsze z k=2. Wyjaśnij, jakie błędy wykrywa każda lista.',
'wyniki_granic = [z44(x, 2) for x in [[10,10,0,0], [0,0,10,10], [5,5,5]]]',
'assert wyniki_granic == [(20,2,0), (20,2,2), (10,2,0)]',
'Testuj najlepszy fragment na obu krańcach.'),
E('Samodzielnie: dokładny zapis średniej',
'Dla pełnych danych utwórz srednia_dokladna jako Fraction z sumy i długości. Porównaj dziesiętny zapis w wyniki4.txt z Fraction; błąd ma być mniejszy niż 1e-9.',
"""from fractions import Fraction
s, d, _ = odp["4.4"]
srednia_dokladna = Fraction(s, d)
with open("wyniki4.txt", "r", encoding="utf-8") as plik:
    wiersze_wyniku = plik.read().splitlines()
zapisana = float(wiersze_wyniku[3].split()[1])
print(srednia_dokladna)""",
'assert abs(zapisana - float(srednia_dokladna)) < 1e-9',
'Fraction przechowuje dokładny ułamek, a nie przybliżenie float.'),
], official='2024_zadanie_4.md')
]
