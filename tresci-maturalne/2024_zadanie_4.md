## Zadanie maturalne — pełna transkrypcja treści CKE

**Źródło:** CKE, egzamin maturalny z informatyki, poziom rozszerzony, Formuła 2023, 22 maja 2024 r., arkusz `MINP-R0-100-2405`, zadanie 4 „Liczby”, łącznie 10 punktów.  
**Oryginalny arkusz:** [arkusz-2024.pdf](materialy-zrodlowe/arkusz-2024.pdf)

Poniżej przepisano treść zadania maturalnego. Zachowano polecenia i przykłady, zmieniając jedynie układ typograficzny. Pominięto puste pola odpowiedzi, punktację na marginesie oraz nagłówki i stopki stron.

### Zadanie 4. Liczby

Plik `liczby.txt` składa się z dwóch wierszy:

- pierwszy wiersz pliku zawiera 3000 liczb pierwszych z przedziału [2, 2000],
- drugi wiersz pliku zawiera 20 liczb całkowitych z przedziału [2, 1 000 000 000].

Liczby w wierszach są rozdzielone znakami spacji.

Napisz program (lub kilka programów), który(-e) znajdzie(-ą) odpowiedzi do podanych zadań. Każdą odpowiedź zapisz w pliku `wyniki4.txt` i poprzedź ją numerem oznaczającym zadanie.

Do Twojej dyspozycji jest plik `liczby_przyklad.txt`, który zawiera 200 liczb w pierwszym wierszu (są to wyłącznie liczby 2, 3, 5, 7 i 31) oraz 20 liczb w drugim wierszu. Odpowiedzi dla danych z tego pliku są umieszczone pod każdym zadaniem.

Pamiętaj, że Twój program musi ostatecznie zadziałać na pliku `liczby.txt` z 3000 liczb w pierwszym wierszu.

### Zadanie 4.1. (0–2)

Podaj, ile liczb z pierwszego wiersza jest dzielnikiem jakiejkolwiek liczby spośród liczb z drugiego wiersza.

Dla pliku `liczby_przyklad.txt` odpowiedzią jest 199 (tylko liczba 31, która występuje raz, nie jest dzielnikiem żadnej z liczb w drugim wierszu).

### Zadanie 4.2. (0–2)

Spośród liczb z pierwszego wiersza podaj liczbę, która jest sto pierwszą liczbą w kolejności, licząc od największej po ich uporządkowaniu.

Przykład: wśród liczb 2, 4, 2, 3, 3, 4 drugą w kolejności, licząc od największej, jest liczba 4.

Dla pliku `liczby_przyklad.txt` odpowiedzią jest 5.

### Zadanie 4.3. (0–3)

Dla każdej z liczb z drugiego wiersza rozstrzygnij, czy da się ją przedstawić jako iloczyn jedynie liczb z pierwszego wiersza. Przy tym liczba wystąpień danego czynnika w iloczynie nie może być większa niż liczba wystąpień tego czynnika w pierwszym wierszu.

Znajdź wszystkie liczby, które da się tak przedstawić, i je wypisz.

Dla pliku `liczby_przyklad.txt` odpowiedzią są liczby:

```text
10 12 14 15 18 20 21 25 27 28
```

(liczbę 16 można przedstawić jako iloczyn 2∙2∙2∙2, jednak w pierwszym wierszu liczba 2 występuje tylko dwa razy, więc 16 nie należy do rozwiązania. Podobnie jest z liczbą 24, którą można przedstawić jako iloczyn 2∙2∙2∙3).

### Zadanie 4.4. (0–3)

Znajdź w ciągu liczb z pierwszego wiersza spójny fragment, który zawiera co najmniej 50 elementów i którego średnia arytmetyczna jest największa.

Jeżeli jest więcej niż jeden taki fragment, wybierz ten, który występuje jako pierwszy w pliku `liczby.txt`.

W odpowiedzi wypisz:

- znalezioną najwyższą średnią,
- liczbę elementów ciągu z tą najwyższą średnią,
- liczbę, która jest pierwszym elementem tego ciągu.

Dla pliku `liczby_przyklad.txt` odpowiedzią jest:

```text
5,52 50 5
```

(największa średnia to 5,52 dla 50 liczb zaczynających się od liczby 5).

Do oceny oddajesz:

- plik `wyniki4.txt` – zawierający odpowiedzi do zadań 4.1.–4.4. (odpowiedź do każdego zadania powinna być poprzedzona jego numerem)
- pliki zawierające kody źródłowe Twojego(-ich) programu(-ów) o nazwach (uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania):
