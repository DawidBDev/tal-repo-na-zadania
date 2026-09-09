from .common import lesson, theory as T, task as E
from .files import FILE_LESSON

LESSONS = [
lesson(1, 'jupyter_i_podstawy_pythona', 'Powtórzenie Pythona: Jupyter, obliczenia i sterowanie',
'Przygotowanie do przetwarzania cyfr, liczników i danych z pliku.',
['Czym różni się wynik wyświetlony na ekranie od wartości przechowywanej w zmiennej?', 'Jaki jest wynik 17 / 5, 17 // 5 i 17 % 5?', 'Dlaczego komórka uruchomiona po restarcie jądra może nie znać zmiennej?'],
[
T(1, 'Komórki, typy i stan programu',
"""Komórka Markdown przechowuje opis; komórka Code wykonuje kod w jądrze Pythona. Shift+Enter uruchamia komórkę i przechodzi dalej. Numer wykonania pokazuje kolejność uruchomień, nie położenie na stronie. Zmienna istnieje dopiero po wykonaniu przypisania. Uruchomienie komórki ponownie może zmienić wynik, jeśli kod korzysta ze starej wartości.

int przechowuje liczby całkowite, float przybliżenia liczb rzeczywistych, str tekst, bool True albo False. Wcięcie o cztery spacje wyznacza blok. print wypisuje dane, a assert warunek przerywa wykonanie, gdy warunek jest fałszywy. To prosty test poprawności.""",
"""liczba = 7
liczba += 1
print(liczba, type(liczba))
assert liczba == 8
print("7" + "3", 7 + 3)"""),
T(3, 'Dzielenie, konwersja i warunki',
"""Operator / zawsze daje wynik rzeczywisty. // zaokrągla iloraz w dół: -7 // 3 daje -3. Dla dodatnich liczb jest to liczba pełnych grup. Reszta n % p należy do zakresu od 0 do p-1, gdy p jest dodatnie. Zachodzi n == (n // p) * p + n % p.

int("17") zamienia zapis liczby na liczbę. Użyj == do porównania; = przypisuje. Warunki łączymy przez and, or i not. W if/elif/else wykonywany jest tylko pierwszy spełniony wariant. Przed dzieleniem sprawdź, czy dzielnik nie jest zerem.""",
"""n = 125
print(n // 60, n % 60)
punkty = 72
if punkty >= 80:
    opis = "bardzo dobry"
elif punkty >= 50:
    opis = "zaliczony"
else:
    opis = "do poprawy"
print(opis)"""),
T(6, 'Pętla, licznik i akumulator',
"""range(a, b) obejmuje a i wyklucza b. range(1, n + 1) przechodzi przez liczby od 1 do n. Licznik zwiększasz tylko po spełnieniu warunku; akumulator powiększasz o wartość elementu.

while powtarza kod tak długo, jak warunek jest prawdziwy. W każdej iteracji musi nastąpić postęp prowadzący do zakończenia. Licznik i sumę inicjalizuj przed pętlą; po restarcie i uruchomieniu całej karty wynik ma być taki sam.""",
"""suma = 0
ile = 0
for n in range(1, 11):
    if n % 2 == 0:
        suma += n
        ile += 1
print(ile, suma)
assert (ile, suma) == (5, 30)"""),
],
[
E('Przewidź, uruchom, wyjaśnij',
'Bez uruchamiania oblicz wynik a=8; b=a; a+=5. Zapisz wartości a i b, następnie wykonaj kod. Zmienna przewidywanie ma zawierać parę oczekiwanych wartości. Wyjaśnij, dlaczego b się nie zmienia.',
"""a = 8
b = a
a += 5
przewidywanie = (13, 8)""",
'assert przewidywanie == (a, b) == (13, 8)',
'Przypisanie nazwy b do liczby nie tworzy formuły zależnej od a.'),
E('Powtarzalny notatnik',
'Ustaw licznik na 0, zwiększ go trzykrotnie i zapisz w wynik_stanu. Uruchom komórkę dwa razy, a następnie po restarcie. Za każdym razem wynik ma wynosić 3. Wyjaśnij rolę inicjalizacji.',
"""licznik = 0
licznik += 1
licznik += 1
licznik += 1
wynik_stanu = licznik""",
'assert wynik_stanu == 3',
'Zerowanie musi należeć do komórki, którą powtarzasz.'),
E('Czas w sekundach',
"Dla tekstu '3671' oblicz h, m, s bez liczb rzeczywistych. Wynik: 1 godzina, 1 minuta i 11 sekund. Wypisz wynik w formacie 01:01:11. Sprawdź również 59 i 3600 sekund.",
"""sekundy = int("3671")
h = sekundy // 3600
m = (sekundy % 3600) // 60
s = sekundy % 60
zapis = f"{h:02d}:{m:02d}:{s:02d}"
print(zapis)""",
"""assert (h, m, s) == (1, 1, 11)
assert zapis == "01:01:11"
""",
'Najpierw wydziel godziny, potem pracuj na pozostałych sekundach.'),
E('Dzielniki bez pułapki logicznej',
'Dla n=30 zapisz w czy_dzielne informację, czy n jest podzielne przez 3 i przez 5. Zmień n na 9: wynik ma być False. Wyjaśnij różnicę między and i or.',
"""n = 30
czy_dzielne = n % 3 == 0 and n % 5 == 0""",
"""assert czy_dzielne is True
assert not (9 % 3 == 0 and 9 % 5 == 0)""",
'Oba porównania muszą być osobnymi wyrażeniami.'),
E('Progi i wartości graniczne',
"Dla 0 <= punkty <= 100 przypisz kategorie: poniżej 50 'N', 50–79 'P', od 80 'B'. Rozwiąż dla punkty=80 i uzasadnij działanie dla 49, 50 i 79.",
"""punkty = 80
if punkty >= 80:
    kategoria = "B"
elif punkty >= 50:
    kategoria = "P"
else:
    kategoria = "N" """,
'assert kategoria == "B"',
'Ułóż progi od najwyższego albo zapewnij rozłączne przedziały.'),
E('Filtrowanie i sumowanie',
'Pętlą policz, ile liczb od 1 do 30 jest podzielnych przez 4, ale nie przez 3. Zapisz liczność w ile, a sumę w suma. Wynik: 5 liczb o sumie 76.',
"""ile = 0
suma = 0
for n in range(1, 31):
    if n % 4 == 0 and n % 3 != 0:
        ile += 1
        suma += n""",
'assert (ile, suma) == (5, 76)',
'Odrzuć 12 i 24, choć są wielokrotnościami 4.'),
E('Najmniejsza wystarczająca potęga',
'Dla n=70 znajdź p, najmniejszą potęgę dwójki nie mniejszą od n. Użyj while. Policz wykonane podwojenia w kroki. Wynik: 128 i 7. Sprawdź myślowo n=1 i n=64.',
"""n = 70
p = 1
kroki = 0
while p < n:
    p *= 2
    kroki += 1""",
'assert (p, kroki) == (128, 7)',
'Pierwszą potęgą jest 2**0, czyli 1.'),
E('Mini-analiza jak w arkuszu',
'Dla liczb 100–150 policz te, których cyfra jedności jest nieparzysta, a suma cyfry setek i jedności wynosi 6. Zapisz liczność, sumę i największą taką liczbę. Wynik: 5, 625, 145. Wydziel cyfry arytmetycznie.',
"""ile = suma = 0
najwieksza = None
for n in range(100, 151):
    jednosci = n % 10
    setki = n // 100
    if jednosci % 2 == 1 and setki + jednosci == 6:
        ile += 1
        suma += n
        najwieksza = n""",
'assert (ile, suma, najwieksza) == (5, 625, 145)',
'Wszystkie rozważane liczby mają cyfrę setek 1.'),
E('Samodzielnie: cyfry liczby',
'Dla n=407 oblicz sumę trzech cyfr oraz liczbę z cyframi zapisanymi odwrotnie. Użyj // i %. Wynik: 11 oraz 704.',
"""n = 407
a = n // 100
b = n // 10 % 10
c = n % 10
suma_cyfr = a + b + c
odwrotna = 100 * c + 10 * b + a""",
'assert (suma_cyfr, odwrotna) == (11, 704)',
'Zero w środku też jest cyfrą.'),
E('Samodzielnie: wykryj błąd granicy',
'Policz sumę kwadratów od 1 do 10 włącznie. Popraw pomysł range(1,10), wyjaśnij błąd i zapisz odpowiedź w suma_kwadratow.',
"""suma_kwadratow = 0
for n in range(1, 11):
    suma_kwadratow += n * n""",
'assert suma_kwadratow == 385',
'Prawa granica range nie jest wykonywana.'),
], official=None),
lesson(2, 'kolekcje_napisy_i_funkcje', 'Powtórzenie: napisy, kolekcje i funkcje',
'Palindromy, filtrowanie rekordów i liczniki potrzebne w obu maturach.',
['Jakie indeksy mają pierwszy i ostatni element listy długości 5?', 'Co zwraca funkcja bez instrukcji return?', 'Kiedy trzeba zachować powtórzenia danych?'],
[
T(1, 'Napis i lista: indeksy oraz kopie',
"""str jest niezmiennym ciągiem znaków. s[1:4] wybiera indeksy 1, 2, 3; s[::-1] odwraca napis. Lista przechowuje dowolne obiekty i może się zmieniać: append dodaje na koniec.

Przypisanie b = a dla list nie kopiuje danych: obie nazwy wskazują tę samą listę. b = a.copy() tworzy płytką kopię, wystarczającą dla listy liczb. Nie usuwaj elementów listy podczas przechodzenia po niej; buduj nową listę.""",
"""a = [2, 4]
b = a.copy()
b.append(8)
print(a, b)
s = "informatyka"
print(s[0], s[-1], s[2:5], s[::-1])"""),
T(3, 'Funkcja i kontrakt',
"""def tworzy funkcję. Parametry opisują dane wejściowe, return przekazuje wynik do miejsca wywołania. Wypisanie wyniku przez print nie zastępuje return. Kontrakt określa dopuszczalne argumenty i znaczenie zwracanej wartości.

Testuj przypadek typowy, minimalny i graniczny. None może oznaczać brak wyniku; nie jest liczbą 0. Funkcja nie powinna korzystać z przypadkowo utworzonej wcześniej zmiennej globalnej.""",
"""def roznica(a, b):
    return a - b

assert roznica(8, 3) == 5
assert roznica(3, 8) == -5
print(roznica(2, 2))"""),
T(6, 'Krotka, słownik i zbiór',
"""Krotka (x, y) opisuje parę i może być kluczem słownika albo elementem zbioru. Rozpakowanie x, y = punkt daje osobne współrzędne.

Słownik kojarzy klucz z wartością. get(k, 0) zwraca 0 dla brakującego klucza. Zbiór set usuwa powtórzenia i przyspiesza sprawdzanie przynależności; nie używaj go do zliczania wszystkich wystąpień. enumerate(lista, start=1) wiąże dane z numerem wiersza liczonym od 1.""",
"""licznosci = {}
for znak in "ABBA":
    licznosci[znak] = licznosci.get(znak, 0) + 1
print(licznosci)
for numer, wartosc in enumerate([7, 7, 9], start=1):
    print(numer, wartosc)"""),
],
[
E('Indeksy i wycinki',
"Dla s='matura' utwórz krotkę wycinki: pierwszy znak, ostatni znak, znaki o indeksach 1–3 i odwrócony napis.",
"""s = "matura"
wycinki = (s[0], s[-1], s[1:4], s[::-1])""",
'assert wycinki == ("m", "a", "atu", "arutam")',
'Koniec wycinka jest wyłączony.'),
E('Kopia danych',
'Utwórz lista_a=[3,1,3] i jej kopię lista_b. Dopisz 9 tylko do lista_b. Zapisz, co stałoby się po lista_b=lista_a.',
"""lista_a = [3, 1, 3]
lista_b = lista_a.copy()
lista_b.append(9)""",
"""assert lista_a == [3, 1, 3]
assert lista_b == [3, 1, 3, 9]""",
'Użyj copy, a nie samego przypisania.'),
E('Filtr jako funkcja',
'Napisz dodatnie(liczby), zwracającą nową listę elementów >0 w kolejności wejścia. Nie zmieniaj argumentu.',
"""def dodatnie(liczby):
    wynik = []
    for n in liczby:
        if n > 0:
            wynik.append(n)
    return wynik""",
"""assert dodatnie([-2, 0, 5, 5]) == [5, 5]
assert dodatnie([]) == []""",
'Potrzebujesz listy wynikowej i return po pętli.'),
E('Palindrom dwoma wskaźnikami',
'Napisz palindrom(s) bez odwracania napisu. Porównuj znaki symetryczne. Pusty napis i pojedynczy znak uznaj za palindromy.',
"""def palindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True""",
"""assert palindrom("kajak")
assert palindrom("")
assert palindrom("x")
assert not palindrom("ab")""",
'Dla i=0 drugim indeksem jest len(s)-1.'),
E('Wynik i numer wiersza',
'Napisz pierwsze_max(liczby), zwracającą parę (maksimum, numer od 1). Przy remisie zachowaj pierwszy wiersz; dla pustej listy zwróć None.',
"""def pierwsze_max(liczby):
    if not liczby:
        return None
    najlepsza = liczby[0]
    numer = 1
    for i, n in enumerate(liczby, start=1):
        if n > najlepsza:
            najlepsza, numer = n, i
    return najlepsza, numer""",
"""assert pierwsze_max([3, 8, 8, 2]) == (8, 2)
assert pierwsze_max([]) is None""",
'Przy równości nie aktualizuj zapamiętanego indeksu.'),
E('Histogram znaków',
'Napisz histogram(s), zwracającą słownik liczności znaków bez Counter. Wielkość liter ma znaczenie.',
"""def histogram(s):
    wynik = {}
    for znak in s:
        wynik[znak] = wynik.get(znak, 0) + 1
    return wynik""",
"""assert histogram("o+o*o") == {"o": 3, "+": 1, "*": 1}
assert histogram("") == {}""",
'Brakujący znak ma dotychczasową liczność zero.'),
E('Usuwanie duplikatów z zachowaniem kolejności',
'Napisz unikalne(dane). [4,2,4,7,2] ma dać [4,2,7]. Użyj listy wynikowej i zbioru wartości już napotkanych.',
"""def unikalne(dane):
    widziane = set()
    wynik = []
    for n in dane:
        if n not in widziane:
            widziane.add(n)
            wynik.append(n)
    return wynik""",
"""assert unikalne([4, 2, 4, 7, 2]) == [4, 2, 7]
assert unikalne([]) == []""",
'Sam set nie przechowuje kolejności potrzebnej do tego zadania.'),
E('Raport o napisach',
'Napisz raport_napisow(napisy): zwróć parę (lista palindromów, słownik liczności długości). Zachowaj kolejność i powtarzające się palindromy. Połącz wcześniejsze funkcje.',
"""def raport_napisow(napisy):
    znalezione = []
    dlugosci = {}
    for s in napisy:
        if palindrom(s):
            znalezione.append(s)
        dlugosci[len(s)] = dlugosci.get(len(s), 0) + 1
    return znalezione, dlugosci""",
'assert raport_napisow(["aa", "ab", "x", "aa"]) == (["aa", "x", "aa"], {2: 3, 1: 1})',
'Nie zastępuj listy znalezionych napisów zbiorem.'),
E('Samodzielnie: anagramy',
'Napisz anagramy(a,b). Porównuj dokładnie znaki, bez ignorowania spacji i wielkości liter. Wykorzystaj histogramy.',
"""def anagramy(a, b):
    return histogram(a) == histogram(b)""",
"""assert anagramy("kot", "tok")
assert not anagramy("aa", "ab")""",
'Kolejność nie jest ważna, liczności są.'),
E('Samodzielnie: najdłuższy napis',
'Napisz najdluzszy(napisy), zwracającą pierwszy najdłuższy napis; dla pustej listy None. Nie sortuj całej listy.',
"""def najdluzszy(napisy):
    wynik = None
    for s in napisy:
        if wynik is None or len(s) > len(wynik):
            wynik = s
    return wynik""",
"""assert najdluzszy(["ab", "cd", "x"]) == "ab"
assert najdluzszy([]) is None""",
'Jedno przejście po liście wystarczy.'),
], official=None),
FILE_LESSON,
lesson(4, 'cyfry_skroty_i_nwd', 'Cyfry, podstawy systemów liczbowych i NWD',
'Przygotowanie nieparzystego skrótu oraz fundament konwersji do systemu trójkowego.',
['Jak wydzielić ostatnią cyfrę liczby bez używania str?', 'Co oznacza zapis 1011 w systemie dwójkowym?', 'Dlaczego NWD(a,b) = NWD(b,a % b)?'],
[
T(1, 'Pozycja cyfry i podstawa systemu',
"""W systemie o podstawie p cyfry mają wartości od 0 do p-1. Wagi od prawej to 1,p,p²,... . Zapis 1011₂ oznacza 1·8+0·4+1·2+1=11. 102₃ oznacza 1·9+0·3+2=11. W systemie szesnastkowym A–F oznaczają 10–15.

Do wydzielenia ostatniej cyfry dowolnego systemu służy n % p; n // p usuwa tę cyfrę. Zero wymaga osobnej uwagi: ma jedną cyfrę, chociaż while n > 0 nie wykona się ani razu.""",
"""n = 45
reszty = []
while n > 0:
    reszty.append(n % 2)
    n //= 2
print(reszty)  # cyfry od najmniej znaczącej
print(list(reversed(reszty)))"""),
T(3, 'Horner i budowanie liczby',
"""Czytając cyfry od lewej, aktualizujemy wartosc = wartosc * podstawa + cyfra. Po każdym kroku wartosc oznacza już przetworzony prefiks. Przy zamianie liczby na zapis reszty pojawiają się odwrotnie, dlatego odwracamy je na końcu.

W nieparzystym skrócie czytamy dziesiętne cyfry od prawej, ale zachowujemy ich kolejność w wyniku. Mnożnik pozycji zwiększamy tylko wtedy, gdy cyfrę rzeczywiście dołączamy. Zero jako wynik pomocniczy może oznaczać brak skrótu: istniejący skrót jest dodatni.""",
"""wartosc = 0
for cyfra in [1, 0, 2]:
    wartosc = wartosc * 3 + cyfra
assert wartosc == 11
print(wartosc)"""),
T(6, 'Algorytm Euklidesa',
"""Każdy wspólny dzielnik a i b dzieli również resztę a % b. Zastąpienie pary (a,b) przez (b,a % b) zachowuje NWD, a druga liczba maleje, aż stanie się zerem.

Na końcu a jest wynikiem. Dla dowolnych znaków argumentów najpierw bierzemy wartości bezwzględne. Dla b=0 wynikiem jest |a|. W kursie NWD(0,0) przyjmujemy jako 0. W 3.1 matury 2024 ograniczenia dotyczą operacji wewnątrz funkcji skrótu: stosujemy tam wyłącznie arytmetykę całkowitą.""",
"""a, b = 84, 35
while b != 0:
    print(a, b, a % b)
    a, b = b, a % b
print("NWD:", a)"""),
],
[
E('Ostatnia cyfra',
'Napisz rozdziel(n,p), zwracającą (iloraz, reszta). Załóż n>=0 i 2<=p<=16. Sprawdź 45 dla podstawy 2 oraz 255 dla 16.',
"""def rozdziel(n, p):
    return n // p, n % p""",
"""assert rozdziel(45, 2) == (22, 1)
assert rozdziel(255, 16) == (15, 15)""",
'Reszta nie musi być pojedynczą cyfrą dziesiętną.'),
E('Suma i liczba cyfr',
'Napisz statystyka_cyfr(n), bez str, zwracającą (suma cyfr, liczba cyfr) dla n>=0. Dla 0: (0,1), dla 407: (11,3).',
"""def statystyka_cyfr(n):
    if n == 0:
        return 0, 1
    suma = ile = 0
    while n > 0:
        suma += n % 10
        ile += 1
        n //= 10
    return suma, ile""",
"""assert statystyka_cyfr(0) == (0, 1)
assert statystyka_cyfr(407) == (11, 3)""",
'Obsłuż zero przed pętlą.'),
E('Horner dla dowolnej podstawy',
'Napisz horner(cyfry,p), przyjmującą listę cyfr od lewej, 2<=p<=16. Użyj assert do sprawdzenia zakresu każdej cyfry. [1,0,1,1] w bazie 2 daje 11, [15,15] w bazie 16 daje 255.',
"""def horner(cyfry, p):
    wynik = 0
    for c in cyfry:
        assert 0 <= c < p
        wynik = wynik * p + c
    return wynik""",
"""assert horner([1, 0, 1, 1], 2) == 11
assert horner([15, 15], 16) == 255""",
'Nie obliczaj za każdym razem całej potęgi; rozszerz dotychczasowy prefiks.'),
E('Liczba na cyfry',
'Napisz cyfry_w_bazie(n,p), zwracającą listę cyfr od lewej dla n>=0 i p>=2. Dla zera zwróć [0]. Sprawdź konwersję tam i z powrotem dla liczb 0–50 w bazie 3.',
"""def cyfry_w_bazie(n, p):
    if n == 0:
        return [0]
    wynik = []
    while n > 0:
        wynik.append(n % p)
        n //= p
    return wynik[::-1]""",
"""assert cyfry_w_bazie(11, 3) == [1, 0, 2]
for n in range(51):
    assert horner(cyfry_w_bazie(n, 3), 3) == n""",
'Kolejność reszt jest przeciwna do kolejności zapisu.'),
E('Nieparzysty skrót',
'Napisz skrot(n) dla n>0. Zostaw tylko cyfry nieparzyste, zachowując kolejność. Zwróć 0, jeżeli skrót nie istnieje. Nie używaj napisów, list ani funkcji wbudowanych wewnątrz skrot.',
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
'Pozycję zwiększ tylko po zachowanej cyfrze.'),
E('Własne NWD',
'Napisz nwd(a,b) algorytmem Euklidesa. Obsłuż wartości ujemne i zero. Porównaj z ręcznym wynikiem dla (84,35).',
"""def nwd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a""",
"""assert nwd(84, 35) == 7
assert nwd(-8, 0) == 8
assert nwd(0, 0) == 0""",
'Jednoczesne przypisanie korzysta ze starych wartości a i b.'),
E('Dwa warunki na jednym rekordzie',
'Napisz wybierz(dane), zachowującą liczby z istniejącym skrótem i NWD liczby oraz skrótu równym 7. Zachowaj kolejność. Dla [224,4872,23527,123] wynik: [4872,23527].',
"""def wybierz(dane):
    wynik = []
    for n in dane:
        m = skrot(n)
        if m != 0 and nwd(n, m) == 7:
            wynik.append(n)
    return wynik""",
'assert wybierz([224, 4872, 23527, 123]) == [4872, 23527]',
'Wylicz skrót raz dla każdego rekordu.'),
E('Dwa niezależne opisy liczby',
"""Napisz raport_liczby(n), zwracającą (skrót, liczba jedynek w zapisie binarnym). Użyj funkcji z tej karty. Dla 13: (13,3), dla 224: (0,3). Wyjaśnij, czemu filtrowanie cyfr dziesiętnych nie jest filtrowaniem bitów.

Plik liczby-trening.txt zawiera po jednej liczbie w wierszu. Sam go otwórz i wczytaj do lista_z_pliku. Dla każdej liczby oblicz raport; zapisz raporty_z_pliku oraz plik wyniki-trening.txt, po jednym wierszu: liczba, skrót, liczba jedynek.""",
"""def raport_liczby(n):
    return skrot(n), sum(cyfry_w_bazie(n, 2))

with open("liczby-trening.txt", "r", encoding="utf-8") as plik:
    lista_z_pliku = [int(wiersz) for wiersz in plik]
raporty_z_pliku = [raport_liczby(n) for n in lista_z_pliku]
with open("wyniki-trening.txt", "w", encoding="utf-8") as plik:
    for n, (sk, jedynki) in zip(lista_z_pliku, raporty_z_pliku):
        print(n, sk, jedynki, file=plik)""",
"""assert raport_liczby(13) == (13, 3)
assert raport_liczby(224) == (0, 3)
assert lista_z_pliku == [13, 224, 45, 101]
assert raporty_z_pliku == [(13, 3), (0, 3), (5, 4), (11, 4)]""",
'Podstawa określa znaczenie pozycji i zbiór cyfr.'),
E('Samodzielnie: NWW',
'Napisz nww(a,b) dla nieujemnych liczb. Jeśli choć jedna jest zerem, zwróć 0. Wykorzystaj NWD i dzielenie całkowite przed mnożeniem.',
"""def nww(a, b):
    if a == 0 or b == 0:
        return 0
    return a // nwd(a, b) * b""",
"""assert nww(12, 18) == 36
assert nww(0, 5) == 0""",
'Iloczyn NWD i NWW jest iloczynem dodatnich argumentów.'),
E('Samodzielnie: zapis szesnastkowy',
'Napisz szesnastkowo(n) dla n>=0. Użyj cyfry_w_bazie i alfabetu 0123456789ABCDEF. Nie używaj hex w implementacji; użyj go do porównania wyników.',
"""def szesnastkowo(n):
    alfabet = "0123456789ABCDEF"
    return "".join(alfabet[c] for c in cyfry_w_bazie(n, 16))""",
"""assert szesnastkowo(255) == "FF"
for n in range(256):
    assert szesnastkowo(n) == hex(n)[2:].upper()""",
'Cyfra o wartości 15 jest reprezentowana przez F.'),
], official=None)
]
