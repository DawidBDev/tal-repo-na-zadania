## Zadanie maturalne — pełna transkrypcja treści CKE

**Źródło:** CKE, egzamin maturalny z informatyki, poziom rozszerzony, Formuła 2023, 22 maja 2024 r., arkusz `MINP-R0-100-2405`, zadanie 3 „Nieparzysty skrót”, łącznie 10 punktów.  
**Oryginalny arkusz:** [arkusz-2024.pdf](materialy-zrodlowe/arkusz-2024.pdf)

Poniżej przepisano treść zadania maturalnego. Zachowano polecenia i przykłady, zmieniając jedynie układ typograficzny. Pominięto puste pola odpowiedzi, punktację na marginesie oraz nagłówki i stopki stron.

### Zadanie 3. Nieparzysty skrót

Nieparzystym skrótem dodatniej liczby całkowitej `n` nazwiemy dodatnią liczbę całkowitą `m`, która powstaje przez usunięcie cyfr parzystych z zapisu dziesiętnego liczby `n`.

Nieparzysty skrót liczby całkowitej `n` nie istnieje, gdy jej zapis dziesiętny składa się tylko z cyfr parzystych.

Przykład:

- Nieparzystym skrótem liczby 294762 jest liczba 97.
- Nieparzystym skrótem liczby 39101 jest liczba 3911.
- Nieparzysty skrót liczby 224 nie istnieje.

### Zadanie 3.1. (0–3)

W postaci pseudokodu lub w wybranym języku programowania napisz funkcję, która dla dodatniej całkowitej liczby `n`, takiej że istnieje dla niej nieparzysty skrót, wyznaczy liczbę `m` – nieparzysty skrót liczby `n`.

**Uwaga:** Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz może operować wyłącznie na liczbach całkowitych. W zapisie możesz wykorzystać tylko operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, resztę z dzielenia oraz porównywanie liczb, instrukcje sterujące, przypisania do zmiennych lub samodzielnie napisane funkcje, wykorzystujące wyżej wymienione operacje. Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione.

**Specyfikacja:**

- Dane: `n` – dodatnia liczba całkowita, taka że istnieje dla niej nieparzysty skrót.
- Wynik: `m` – nieparzysty skrót liczby `n`.

### Zadanie 3.2. (0–3)

Plik `skrot.txt` zawiera 200 dodatnich liczb całkowitych, mniejszych od 30 000. Każda liczba jest zapisana w osobnym wierszu. Dla co najmniej jednej z tych liczb nie istnieje nieparzysty skrót.

Napisz program, który wyznaczy liczbę wszystkich liczb z pliku `skrot.txt`, dla których nie istnieje nieparzysty skrót, oraz poda największą z nich. Odpowiedź zapisz w pliku `wyniki3_2.txt`.

Plik `skrot_przyklad.txt` zawiera 20 liczb mniejszych od 30 000. Dla danych zawartych w pliku `skrot_przyklad.txt` prawidłową odpowiedzią jest:

```text
2
2428
```

(w pliku są dwie liczby, dla których nie istnieje nieparzysty skrót: 266 i 2428; 2428 jest największą z nich).

Do oceny oddajesz:

- plik `wyniki3_2.txt` – zawierający odpowiedź do zadania 3.2.
- plik(-i) zawierający(-e) kod(-y) źródłowy(-e) Twojego programu o nazwie(-ach) (uwaga: brak tego(tych) pliku(-ów) jest równoznaczny z brakiem rozwiązania zadania):

### Zadanie 3.3. (0–4)

Plik `skrot2.txt` zawiera 200 dodatnich liczb całkowitych, mniejszych od 30 000. Każda liczba jest zapisana w osobnym wierszu. Dla każdej z tych liczb istnieje nieparzysty skrót.

Napisz program, który wypisze te liczby z pliku `skrot2.txt`, dla których największy wspólny dzielnik liczby i jej nieparzystego skrótu jest równy 7. Odpowiedź zapisz w pliku `wyniki3_3.txt`. Twój program powinien wypisać w każdym wierszu wyniku po jednej liczbie z pliku `skrot2.txt`, dla której jest spełniony powyższy warunek.

Plik `skrot2_przyklad.txt` zawiera 20 liczb spełniających warunki zadania. Dla danych zawartych w pliku `skrot2_przyklad.txt` prawidłową odpowiedzią jest:

```text
4872
23527
```

Do oceny oddajesz:

- plik `wyniki3_3.txt` – zawierający odpowiedź do zadania 3.3.
- plik(-i) zawierający(-e) kod(-y) źródłowy(-e) Twojego programu o nazwie(-ach) (uwaga: brak tego(tych) pliku(-ów) jest równoznaczny z brakiem rozwiązania zadania):
