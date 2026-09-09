# Kartkówki przed lekcjami 1–12 — Python

Materiał prowadzącego. Nie jest częścią prezentacji ani paczek dla ucznia.

Każdy zestaw jest przeznaczony na **10 minut**, bez komputera i notatek. Zawiera trzy pytania; za każde przyznajemy jeden plus albo minus. Wymagamy odpowiedzi na wszystkie elementy danego pytania. Dopuszczamy inne poprawne implementacje niż w kluczu. Sposób łączenia plusów określa plik 00 z zasadami zajęć.

Przed lekcją 1 sprawdzamy podstawy Pythona znane sprzed kursu. Następne kartkówki odwołują się wyłącznie do wcześniejszych kart. Pytania należy rozdać bez klucza umieszczonego na końcu tego pliku.

## Przed lekcją 1 — podstawy Pythona

Zakres: wcześniej poznane typy, operatory, warunki i pętle.

1. Podaj wartości i typy wyrażeń: `17 // 5`, `17 % 5`, `17 / 5`.
2. Co wypisze kod? Wyjaśnij, które liczby zostały dodane.

```python
suma = 0
for n in range(1, 7):
    if n % 2 == 0:
        suma += n
print(suma)
```

3. Napisz funkcję `wieksza(a, b)`, zwracającą większą z dwóch liczb. Przy równych argumentach zwróć ich wspólną wartość. Nie zastępuj `return` przez `print`.

## Przed lekcją 2 — powtórzenie lekcji 1

Zakres: przypisanie, warunki, inicjalizacja i granice pętli.

1. Jakie wartości wypisze kod? Dlaczego `b` nie zmienia się po ostatnim przypisaniu?

```python
a = 8
b = a
a += 5
print(a, b)
```

2. Napisz warunek sprawdzający, czy dodatnia liczba `n` jest podzielna przez 4, ale nie przez 3.
3. Napisz kod obliczający sumę kwadratów liczb od 1 do 5 włącznie. Zainicjalizuj sumę tak, żeby ponowne wykonanie całej komórki dało ten sam wynik.

## Przed lekcją 3 — powtórzenie lekcji 2

Zakres: listy, kopie, funkcje i słowniki.

1. Podaj zawartość `a`, `b` i `c` po wykonaniu kodu. Wskaż, które przypisanie tworzy kopię listy.

```python
a = [2, 4]
b = a
c = a.copy()
b.append(8)
```

2. Napisz funkcję `palindrom(s)`, zwracającą informację, czy napis czytany od przodu i od tyłu jest taki sam. Jaki wynik otrzymasz dla pustego napisu?
3. Podaj końcową zawartość `licznik`. Wyjaśnij znaczenie drugiego argumentu `get`.

```python
licznik = {}
for znak in "ABBAA":
    licznik[znak] = licznik.get(znak, 0) + 1
```

## Przed lekcją 4 — powtórzenie lekcji 3

Zakres: samodzielny odczyt pliku, konwersja i zapis.

1. Plik `liczby.txt` leży obok notatnika i zawiera po jednej liczbie całkowitej w wierszu. Napisz cały kod otwierający plik i wczytujący liczby do listy `liczby`. Nie zakładaj, że plik został już otwarty.
2. Jaką listę otrzymasz po wykonaniu `" 12\t -3  0 ".split()`? Co trzeba zrobić, aby otrzymać liczby zamiast napisów?
3. Napisz kod otwierający `wynik.txt` i zapisujący w nim sumę elementów istniejącej listy `liczby`. Wyjaśnij, co tryb `"w"` zrobi z wcześniejszą zawartością tego pliku.

## Przed lekcją 5 — powtórzenie lekcji 4

Zakres: systemy pozycyjne, nieparzysty skrót i NWD.

1. Zamień `10110₂` na zapis dziesiętny. Pokaż składniki sumy wynikające z wag pozycji.
2. Wyznacz nieparzysty skrót liczb `294762` i `224`. Podaj operatory potrzebne do wydzielenia i usunięcia ostatniej cyfry dziesiętnej bez używania napisów.
3. Oblicz `NWD(84, 35)` algorytmem Euklidesa. Zapisz kolejne dzielenia z resztą aż do reszty zero.

## Przed lekcją 6 — powtórzenie lekcji 5

Zakres: filtrowanie według skrótu, NWD i kompletne zadanie plikowe.

1. Dla liczb `[266, 97, 2428, 135]` podaj liczbę rekordów bez nieparzystego skrótu oraz największy taki rekord. Uzasadnij wybór.
2. Dlaczego podzielność liczby i jej skrótu przez 7 nie wystarcza, żeby stwierdzić, że ich NWD jest równy 7? Jako kontrprzykład użyj liczby `77` i jej skrótu.
3. Masz własną funkcję `skrot(n)`, która zwraca zero przy braku skrótu. Napisz cały kod otwierający plik `liczby.txt` (jedna liczba na wiersz), zliczający rekordy bez skrótu i wyświetlający liczność.

## Przed lekcją 7 — powtórzenie lekcji 6

Zakres: ranking, wystąpienia dzielników i ograniczony zapas czynników.

1. Jaka jest druga największa liczba w `[2, 4, 2, 3, 3, 4]`, jeśli zachowujemy powtórzenia? Podaj indeks tej pozycji w liście posortowanej malejąco i wyjaśnij, dlaczego nie używamy `set`.
2. Pierwsza lista to `[2, 2, 3, 7]`, druga `[12, 15]`. Ile wystąpień z pierwszej listy dzieli przynajmniej jedną liczbę z drugiej? Wypisz te wystąpienia.
3. Masz czynniki `[2, 2, 3, 5]`, każde wystąpienie wolno użyć najwyżej raz. Które z liczb `12`, `16`, `20` można zbudować? Zapisz rozkłady uzasadniające odpowiedź.

## Przed lekcją 8 — powtórzenie lekcji 7

Zakres: prefiksy, dokładne porównanie średnich i granice fragmentów.

1. Dla `a = [3, 1, 8, 2]` wypisz tablicę sum prefiksowych zaczynającą się od zera. Oblicz z niej sumę fragmentu `a[1:3]`.
2. Który fragment ma większą średnią: o sumie 17 i długości 2 czy o sumie 18 i długości 3? Uzasadnij porównaniem całkowitoliczbowym, bez dzielenia.
3. Dla `[0, 0, 9, 9]` i minimalnej długości 2 podaj sumę, długość i indeks początku najlepszego fragmentu. Dlaczego pętla po prawych końcach musi dopuszczać `r = len(a)`?

## Przed lekcją 9 — powtórzenie lekcji 8

Zakres: zadanie „Liczby” i zachowywanie znaczenia danych.

1. Czy przed zadaniem o najlepszym spójnym fragmencie wolno posortować pierwszy wiersz pliku w miejscu? Uzasadnij i podaj sposób utworzenia posortowanej listy do zadania rankingowego bez zmiany oryginału.
2. W zadaniu o ograniczonych czynnikach badamy po kolei liczby z drugiego wiersza. Czy zużycie czynnika podczas badania pierwszej liczby zmniejsza zapas dla następnej? Uzasadnij na przykładzie czynników `[2, 2, 3]` i liczb `[12, 12]`.
3. Dla ciągu `[9, 1, 9]` i minimalnej długości 2 wskaż fragment o największej średniej. Wyjaśnij, dlaczego sprawdzenie wyłącznie fragmentów długości 2 da błędny wynik.

## Przed lekcją 10 — powtórzenie lekcji 9

Zakres: kodowanie trójkowe, palindromy i siatki.

1. Symbole `o`, `+`, `*` oznaczają odpowiednio cyfry 0, 1, 2 systemu trójkowego. Oblicz wartość napisu `+o*` w systemie dziesiętnym i pokaż kolejne wartości akumulatora Hornera.
2. W siatce z czterech wierszy `ooo` ile jest jednolitych kwadratów 3×3? Podaj pozycje środków jako (wiersz, kolumna), licząc od 1. Kwadraty mogą się nakładać.
3. Napisz jeden warunek sprawdzający, czy `s` jest palindromem. Wyjaśnij, dlaczego maksimum liczb zapisanych symbolami wyznaczamy po zdekodowanej wartości, a nie przez zwykłe porównanie napisów.

## Przed lekcją 11 — powtórzenie lekcji 10

Zakres: kontrola rekordów i wyników zadania „Zapis symboliczny”.

1. Plik zawiera dwa jednakowe wiersze `oooo+**+oooo`. Ile wierszy powinno znaleźć się w odpowiedzi dotyczącej palindromów? Wyjaśnij, dlaczego `set` byłby tu błędem.
2. Środek kwadratu ma indeksy Pythona `(5, 2)`. Jaką parę zapiszesz w odpowiedzi maturalnej? Dlaczego usuwanie ostatniego znaku z wiersza otrzymanego przez `splitlines()` jest błędem?
3. Czy suma liczb zapisanych jako 12 symboli zawsze zmieści się w 12 symbolach? Uzasadnij na przykładzie dodania dwóch liczb o zapisie `**` w systemie trójkowym: podaj sumę dziesiętną i jej zapis symboliczny.

## Przed lekcją 12 — powtórzenie lekcji 11

Zakres: położenie a przesunięcie, NWD i środek odcinka.

1. Dron startuje w `(0, 0)` i wykonuje ruchy `(2, 2)`, `(2, 2)`, `(2, -1)`. Wypisz punkty po każdym ruchu i policz, ile leży ściśle wewnątrz kwadratu `0 < x < 5`, `0 < y < 5`.
2. Podaj `NWD(12, -18)` i `NWD(7, 0)` zgodnie z regułą liczenia dla wartości bezwzględnych. Czy obie pary spełniają warunek `NWD > 1`?
3. Wśród punktów `(2, 2)`, `(3, 8)`, `(4, 4)`, `(6, 6)` wskaż trójkę, w której jeden punkt jest środkiem odcinka o końcach w dwóch pozostałych. Zapisz dwie równości całkowitoliczbowe potwierdzające wynik. Czy wystarczyłoby badać tylko trzy kolejne punkty?

## Klucz odpowiedzi — tylko dla prowadzącego

Każdy numer poniżej odpowiada jednemu pytaniu i jednemu znakowi +/−. Poprawny kod może różnić się od wzorca. Przy pytaniach wymagających uzasadnienia sam wynik liczbowy nie jest kompletną odpowiedzią.

### Przed lekcją 1

1. `3` typu `int`, `2` typu `int`, `3.4` typu `float`.
2. `12`; dodane zostały 2, 4 i 6.
3. Przykładowa funkcja:

```python
def wieksza(a, b):
    if a >= b:
        return a
    return b
```

### Przed lekcją 2

1. `13 8`. Liczby całkowite są niezmienne; aktualizacja `a` nie zmienia wartości związanej z `b`.
2. `n % 4 == 0 and n % 3 != 0`.
3. Wynik 55; inicjalizacja musi być częścią wykonywanego kodu:

```python
suma = 0
for n in range(1, 6):
    suma += n * n
```

### Przed lekcją 3

1. `a` i `b`: `[2, 4, 8]`; `c`: `[2, 4]`. Kopię tworzy `a.copy()`.
2. `def palindrom(s): return s == s[::-1]`; pusty napis daje `True`.
3. `{'A': 3, 'B': 2}`. Zero jest wartością domyślną dla brakującego klucza.

### Przed lekcją 4

1. Wymagamy otwarcia, odczytu i konwersji, np.:

```python
liczby = []
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        liczby.append(int(wiersz))
```

2. `['12', '-3', '0']`; konwersja każdego pola przez `int`, np. `[int(x) for x in pola]`.
3. Tryb `w` zastępuje dotychczasową zawartość:

```python
with open("wynik.txt", "w", encoding="utf-8") as plik:
    print(sum(liczby), file=plik)
```

### Przed lekcją 5

1. `1·16 + 0·8 + 1·4 + 1·2 + 0·1 = 22`.
2. 97 oraz brak skrótu (funkcja pomocnicza zwraca 0). Ostatnia cyfra: `n % 10`; usunięcie: `n // 10`.
3. `84 = 2·35 + 14`, `35 = 2·14 + 7`, `14 = 2·7 + 0`; NWD wynosi 7.

### Przed lekcją 6

1. Dwa rekordy: 266 i 2428; maksimum 2428. Wszystkie ich cyfry są parzyste.
2. Skrót 77 to 77. Obie liczby są podzielne przez 7, ale ich NWD wynosi 77, a nie 7.
3. Przykładowy kompletny kod:

```python
ile = 0
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        n = int(wiersz)
        if skrot(n) == 0:
            ile += 1
print(ile)
```

### Przed lekcją 7

1. 4, indeks 1. Zbiór usunąłby powtórzenia i zmienił ranking.
2. Trzy wystąpienia: 2, 2, 3; oba wystąpienia 2 liczymy osobno, a wystąpienie 3 tylko raz mimo dzielenia obu liczb.
3. `12 = 2·2·3` i `20 = 2·2·5` są możliwe. `16 = 2·2·2·2` wymaga czterech dwójek, a są tylko dwie.

### Przed lekcją 8

1. `[0, 3, 4, 12, 14]`; `P[3] - P[1] = 12 - 3 = 9`.
2. Pierwszy fragment; `17·3 = 51 > 18·2 = 36`.
3. `(18, 2, 2)`. Prawy koniec wycinka jest wyłączny; `r = len(a)` pozwala uwzględnić ostatni element.

### Przed lekcją 9

1. Nie — sortowanie zmienia sąsiedztwo i spójne fragmenty. `posortowane = sorted(a, reverse=True)` pozostawia `a` bez zmian.
2. Nie; każdą liczbę badamy niezależnie z pełnym zapasem. Oba wystąpienia 12 można przedstawić jako `2·2·3`.
3. Cały ciąg: średnia `19/3`, większa od `10/2` w obu fragmentach dwuelementowych. Minimalna długość nie oznacza jedynej dopuszczalnej długości.

### Przed lekcją 10

1. Akumulator po znakach: 1, 3, 11; wynik 11.
2. Dwa kwadraty, środki `(2, 2)` i `(3, 2)`.
3. `s == s[::-1]`. Porządek znaków nie odpowiada wartościom cyfr; np. zwykłe porównanie uznaje `o` za większe od `*`, choć 0 < 2.

### Przed lekcją 11

1. Dwa wiersze; odpowiedź zachowuje wystąpienia i kolejność danych.
2. `(6, 3)`. `splitlines()` usunęło już zakończenie; ostatni znak jest właściwym symbolem rekordu.
3. Nie. `**` oznacza 8; `8 + 8 = 16`, czyli `121₃`, zapis `+*+`. Suma potrzebuje dodatkowej pozycji; ten sam mechanizm działa dla 12 cyfr.

### Przed lekcją 12

1. Punkty `(2, 2)`, `(4, 4)`, `(6, 3)`; wewnątrz są dwa pierwsze.
2. 6 i 7; obie pary spełniają warunek.
3. `(2, 2)`, `(4, 4)`, `(6, 6)`; `2·4 = 2+6` dla obu współrzędnych. Nie wystarczy badać sąsiadów, ponieważ punkt `(3, 8)` rozdziela szukane punkty na liście.
