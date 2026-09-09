## Zadanie maturalne — pełna transkrypcja treści CKE

**Źródło:** CKE, egzamin maturalny z informatyki, poziom rozszerzony, Formuła 2023, 14 maja 2025 r., arkusz `MINP-R0-100-2505`, zadanie 2 „Zapis symboliczny”, łącznie 11 punktów.  
**Oryginalny arkusz:** [arkusz-2025.pdf](materialy-zrodlowe/arkusz-2025.pdf)

Poniżej przepisano treść zadania maturalnego. Zachowano polecenia i przykłady, zmieniając jedynie układ typograficzny. Pominięto puste pola odpowiedzi, punktację na marginesie oraz nagłówki i stopki stron. Kwadraty zapisano czcionką o stałej szerokości.

### Zadanie 2. Zapis symboliczny

W pliku `symbole.txt` zapisano 2000 napisów. Każdy z nich jest zapisany w osobnym wierszu i składa się z dokładnie 12 znaków spośród: `o`, `+`, `*`.

Napisz program (lub kilka programów) znajdujący(-ch) odpowiedzi do podanych zadań. Każdą odpowiedź zapisz w pliku `wyniki2.txt` i poprzedź ją numerem oznaczającym zadanie.

Do Twojej dyspozycji jest plik `symbole_przyklad.txt`, który zawiera 20 wierszy danych spełniających warunki zadania. Odpowiedzi dla pliku `symbole_przyklad.txt` są podane pod każdym zadaniem.

Pamiętaj, że Twój program musi ostatecznie zadziałać na pliku `symbole.txt` zawierającym 2000 napisów.

### Zadanie 2.1. (0–2)

Podaj wszystkie takie napisy z pliku `symbole.txt`, które są palindromami (czytane od przodu i od tyłu są takie same). Wypisz je po jednym w wierszu, w kolejności takiej jak w pliku `symbole.txt`.

Odpowiedź dla pliku `symbole_przyklad.txt` to

```text
oooo+**+oooo
```

(w tym pliku jest jeden palindrom)

### Zadanie 2.2. (0–4)

W pliku `symbole.txt` szukamy „kwadratów” złożonych z dziewięciu sąsiadujących identycznych symboli:

```text
+ + +     o o o     * * *
+ + + lub o o o lub * * *
+ + +     o o o     * * *
```

Podaj, ile takich kwadratów występuje w pliku `symbole.txt`. Jeżeli w pliku występuje jeden taki kwadrat, podaj numer wiersza i numer pozycji w wierszu (licząc od 1) jego środkowego pola. Jeżeli jest więcej takich kwadratów, podaj numer wiersza i numer pozycji w wierszu dla środkowego pola każdego z nich.

Przykład:

Poniżej podano 6 wierszy przykładowych danych (po 12 znaków w każdym wierszu):

```text
1. +**+o*o++*o+
2. +++oooo*o***
3. +o*oooo**+++
4. *+*oooooo+++
5. o**o+++o++++
6. oooo++**+*+o
```

Mamy tutaj trzy kwadraty złożone z 9 identycznych symboli: pierwszy ma środek w wierszu 3 na pozycji 5, drugi – w wierszu 3 na pozycji 6, a trzeci – w wierszu 4 na pozycji 11.

Odpowiedź dla pliku `symbole_przyklad.txt` to

```text
1 6 3
```

(jeden kwadrat, który ma środkowe pole w wierszu 6, na pozycji 3).

### Informacja do zadań 2.3. i 2.4.

Każdy z napisów podanych w pliku `symbole.txt` będziemy traktować jako liczbę zapisaną w systemie trójkowym, w którym:

- znak `o` odpowiada cyfrze 0,
- znak `+` odpowiada cyfrze 1,
- znak `*` odpowiada cyfrze 2.

### Zadanie 2.3. (0–2)

Podaj największą liczbę spośród liczb zapisanych w pliku `symbole.txt`. W odpowiedzi podaj tę liczbę w zapisie dziesiętnym oraz napis jej odpowiadający.

Odpowiedź dla pliku `symbole_przyklad.txt` to `519789 ***+o*ooo++o`.

### Zadanie 2.4. (0–3)

Oblicz sumę wszystkich liczb z pliku `symbole.txt`. Podaj jej wartość w zapisie dziesiętnym oraz w zapisie trójkowym z użyciem symboli: `o`, `+`, `*`.

Odpowiedź dla pliku `symbole_przyklad.txt` to `4841542 +oooo****+oo+o+`.

Do oceny oddajesz:

- plik `wyniki2.txt` – zawierający odpowiedzi do zadań 2.1.–2.4. (odpowiedź do każdego zadania powinna być poprzedzona jego numerem)
- pliki zawierające kody źródłowe Twojego(-ich) programu(-ów) o nazwach (uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania):
