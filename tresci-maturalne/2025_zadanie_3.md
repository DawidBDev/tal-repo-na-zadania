## Zadanie maturalne — pełna transkrypcja treści CKE

**Źródło:** CKE, egzamin maturalny z informatyki, poziom rozszerzony, Formuła 2023, 14 maja 2025 r., arkusz `MINP-R0-100-2505`, zadanie 3 „Dron”, łącznie 6 punktów.  
**Oryginalny arkusz:** [arkusz-2025.pdf](materialy-zrodlowe/arkusz-2025.pdf)

Poniżej przepisano treść zadania maturalnego. Zachowano polecenia i przykłady, zmieniając jedynie układ typograficzny. Pominięto puste pola odpowiedzi, punktację na marginesie oraz nagłówki i stopki stron. Wykres przykładu 1 jest dostępny na stronie 10 załączonego PDF; jego współrzędne podano również w treści zadania 3.2.

### Zadanie 3. Dron

Tor lotu pewnego drona składa się z prostych odcinków. Lot rozpoczyna się w punkcie `(0, 0)`, a kończy w punkcie `(20000, 0)`. Dron poza startem i lądowaniem jest zawsze na wysokości większej od zera.

Plik `dron.txt` zawiera 100 wierszy, w których zapisano dane dotyczące ruchu drona. W każdym wierszu jest zapisana para liczb całkowitych rozdzielonych znakiem spacji. Pierwsza liczba oznacza przemieszczenie drona (odległość) w poziomie od ostatniej pozycji – jest to zawsze liczba dodatnia. Druga liczba oznacza przemieszczenie w pionie od ostatniej pozycji. Jeśli druga liczba jest dodatnia, to dron wykonał ruch w górę, jeśli ujemna – w dół, a jeśli równa 0 – nie zmieniał wysokości.

Przykład 1.

Dla przykładowych danych:

```text
3000 2000
2000 9000
5000 -7000
5000 4000
3000 6000
2000 -14000
```

lot drona można zilustrować na wykresie:

[Wykres – strona 10 oryginalnego arkusza](materialy-zrodlowe/arkusz-2025.pdf#page=10)

gdzie:

- x – odległość w poziomie od punktu startowego
- y – wysokość (odległość w pionie od punktu startowego)
- [A, B] – umieszczone na wykresie pary liczb oznaczające przemieszczenia drona odpowiednio w poziomie i w pionie.

Napisz program (lub kilka programów), który(-e) znajdzie(-dą) odpowiedzi dla podanych zadań. Każdą odpowiedź zapisz w pliku `wyniki3.txt` i poprzedź ją numerem oznaczającym zadanie.

Do Twojej dyspozycji jest plik `dron_przyklad.txt` zawierający 10 wierszy danych w opisanej postaci. Odpowiedzi dla pliku `dron_przyklad.txt` są podane pod każdym zadaniem. Pamiętaj, że Twój program musi ostatecznie zadziałać na pliku `dron.txt` zawierającym 100 wierszy danych.

### Zadanie 3.1. (0–2)

Dla każdego przesunięcia `[A, B]` zapisanego w pliku `dron.txt` oblicz największy wspólny dzielnik (NWD) wartości bezwzględnych liczb `A` i `B`. Podaj liczbę par `[A, B]`, dla których największy wspólny dzielnik wartości bezwzględnych liczb `A` i `B` jest większy od 1.

**Uwaga:** przyjmujemy, że `NWD(A, 0) = A`.

Odpowiedź dla pliku `dron_przyklad.txt` to

```text
6
```

### Zadanie 3.2. (0–4)

Rozważmy wszystkie punkty, w których dron znajdował się po wykonaniu kolejnych ruchów (przesunięć).

Dla danych z przykładu 1. będą to punkty: `(3000, 2000)`, `(5000, 11000)`, `(10000, 4000)`, `(15000, 8000)`, `(18000, 14000)` i `(20000, 0)`.

**a)** Podaj, ile spośród wszystkich rozważanych punktów znajduje się wewnątrz kwadratu o wierzchołkach `(0, 0)`, `(0, 5000)`, `(5000, 5000)`, `(5000, 0)`. Nie liczymy punktów leżących na krawędziach kwadratu.

**b)** Spośród wszystkich rozważanych punktów znajdź i podaj trzy różne, takie, że jeden z nich jest środkiem odcinka o końcach w pozostałych dwóch. Jest tylko jedna taka trójka punktów.

**Uwaga:** punkty należące do szukanej trójki nie muszą być trzema kolejnymi punktami, do których przemieszczał się dron.

Odpowiedź dla pliku `dron_przyklad.txt` to:

```text
a) 2
b) (14000, 3014), (16000, 2010), (18000, 1006)
```

Do oceny oddajesz:

- plik `wyniki3.txt` – zawierający odpowiedzi do zadań 3.1.–3.2. (odpowiedź do każdego zadania powinna być poprzedzona jego numerem)
- pliki zawierające kody źródłowe Twojego(-ich) programu(-ów) o nazwach (uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania):
