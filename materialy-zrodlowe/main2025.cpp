#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Zadanie 2

string z2_symbole_txt_path = "../zalaczniki-2025/symbole.txt";

// Zadanie 2.1
bool czyPalindrom2_1(string tekst) {
    int size = tekst.size() - 1;
    for (int i = 0; i < size; i++) {
        if (tekst[i] != tekst[size - i - 1]) {
            return false;
        }
    }
    return true;
}

void Zadanie2_1() {
    ifstream plik(z2_symbole_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik2_1.txt");

    string linia;
    while (getline(plik, linia)) {
        if (czyPalindrom2_1(linia)) {
            cout << linia << endl;
            wynik << linia << endl;
        }
    }

    plik.close();
    wynik.close();
}

// Zadanie 2.2

bool czyKwadrat2_2(string linia[3], int start) {
    char znak = linia[0][start];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (linia[i][start + j] != znak) {
                return false;
            }
        }
    }
    return true;
};

struct wspolrzedne{
    int x;
    int y;
};

void Zadanie2_2() {
    ifstream plik(z2_symbole_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik2_2.txt");

    string linia[3];
    getline(plik, linia[0]);
    getline(plik, linia[1]);
    int row = 1;
    int num = 0;
    struct wspolrzedne wspolrzedne[2000];
    while (getline(plik, linia[2])) {
        for (int i = 0; i< linia->size()-2; i++) {
            if (czyKwadrat2_2(linia, i)) {
                wspolrzedne[num].x = row+1;
                wspolrzedne[num].y = i+2;
                num ++;
            }
        }
        row ++;
        linia[0] = linia[1];
        linia[1] = linia[2];
    }

    cout << num << " ";
    for (int i = 0; i < num; i++) {
        cout << wspolrzedne[i].x << " ";
        cout << wspolrzedne[i].y << " ";
    }

    wynik << num << " ";
    for (int i = 0; i < num; i++) {
        wynik << wspolrzedne[i].x << " ";
        wynik << wspolrzedne[i].y << " ";
    }

    plik.close();
    wynik.close();
}

// Zadanie 2.3

int konwertuj_znak(char znak) {
    if (znak == 'o')
        return 0;
    if (znak == '+')
        return 1;
    return 2;
}

int konwertuj_ciag(string ciag) {
    int len = ciag.length() - 1;
    int suma = 0;
    for (int i = 1, index = len -1; index >= 0; i*=3, index--) {
        suma += konwertuj_znak(ciag[index])*i;;
    }
    return suma;
}

void Zadanie2_3() {
    ifstream plik(z2_symbole_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik2_3.txt");

    string linia;
    getline(plik, linia);
    int max = konwertuj_ciag(linia);
    string max_ciag = linia;
    while (getline(plik, linia)) {
        int now = konwertuj_ciag(linia);
        if (now > max) {
            max = now;
            max_ciag = linia;
        }
    }

    cout << max << " " << max_ciag;

    wynik << max << " " << max_ciag;

    plik.close();
    wynik.close();
}

// Zadanie 2.4

char konwertuj_cyfre(int cyfra) {
    if (cyfra == 0)
        return 'o';
    if (cyfra == 1)
        return '+';
    return '*';
}

string konwertuj_liczbe(int liczba) {

    string result = "";
    if (liczba == 0)
        return result + konwertuj_cyfre(0);
    int max = 1;
    while (max*3 <= liczba) {
        max *= 3;
    }
    for (int i = max; i > 0; i/=3) {
        for (int k = 2; k>=0; k--) {
            if (k*i <= liczba) {
                liczba -= k*i;
                result += konwertuj_cyfre(k);
                break;
            }
        }
    }
    return result;
}

void Zadanie2_4() {
    ifstream plik(z2_symbole_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik2_4.txt");

    string linia;
    int suma = 0;
    while (getline(plik, linia)) {
        suma += konwertuj_ciag(linia);
    }

    cout << suma << " " << konwertuj_liczbe(suma);

    wynik << suma << " " << konwertuj_liczbe(suma);

    plik.close();
    wynik.close();
}

// Zadanie 3

string z3_dron_txt_path = "../zalaczniki-2025/dron.txt";

// Zadanie 3.1
// sito euklidesa - https://www.matemaks.pl/najwiekszy-wspolny-dzielnik-nwd.html
int nwd(int a, int b){
    while (b != 0) {
        int pom = b;
        b = a % b;
        a = pom;
    }
    return a;
}
void Zadanie3_1() {
    ifstream plik(z3_dron_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik3_1.txt");

    int przemieszczenie_x;
    int przemieszczenie_y;
    int licznik = 0;
    while (plik >> przemieszczenie_x >> przemieszczenie_y) {
        if (przemieszczenie_y < 0) {
            przemieszczenie_y *= -1;
        }
        int result = nwd(przemieszczenie_x, przemieszczenie_y);
        if (1 < result) {
            licznik++;
        }
    }

    cout << licznik ;

    wynik << licznik ;

    plik.close();
    wynik.close();
}

// Zadanie 3.2.a

struct prostokat {
    struct wspolrzedne lewy_dolny_rog;
    struct wspolrzedne prawy_gorny_rog;
};

bool czy_punkt_jest_w_kwadracie(wspolrzedne wspolrzedne) {
    prostokat kwadrat;
    kwadrat.lewy_dolny_rog.x = 0;
    kwadrat.lewy_dolny_rog.y = 0;
    kwadrat.prawy_gorny_rog.x = 5000;
    kwadrat.prawy_gorny_rog.y = 5000;

    if (wspolrzedne.x < kwadrat.lewy_dolny_rog.x)
        return false;
    if (wspolrzedne.y < kwadrat.lewy_dolny_rog.y)
        return false;
    if (wspolrzedne.x > kwadrat.prawy_gorny_rog.x)
        return false;
    if (wspolrzedne.y > kwadrat.prawy_gorny_rog.y)
        return false;
    return true;
}

void Zadanie3_2_a() {
    ifstream plik(z3_dron_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik3_2_a.txt");

    int przemieszczenie_x;
    int przemieszczenie_y;
    struct wspolrzedne wspolrzedne;
    wspolrzedne.x = 0;
    wspolrzedne.y = 0;
    int licznik = 0;
    while (plik >> przemieszczenie_x >> przemieszczenie_y) {
        wspolrzedne.x += przemieszczenie_x;
        wspolrzedne.y += przemieszczenie_y;
        if (czy_punkt_jest_w_kwadracie(wspolrzedne)) {
            licznik++;
        }
    }
    cout << licznik ;
    wynik << licznik ;
    plik.close();
    wynik.close();
}

// Zadanie 3.2.b

wspolrzedne srodek(wspolrzedne w1, wspolrzedne w2) {
    wspolrzedne wynik;
    wynik.x = w1.x + (w2.x - w1.x)/2;
    wynik.y = w1.y + (w2.y - w1.y)/2;
    return wynik;
}

void Zadanie3_2_b() {
    ifstream plik(z3_dron_txt_path);
    if (!plik.is_open()) {
        cerr << "Nie udalo sie otworzyc pliku!" << endl;
        return;
    }

    ofstream wynik("../wynik3_2_b.txt");

    int przemieszczenie_x;
    int przemieszczenie_y;
    struct wspolrzedne wsp[100];
    plik >> wsp[0].x >> wsp[0].y;

    for (int i = 1;plik >> przemieszczenie_x >> przemieszczenie_y ; i++ ) {
        wsp[i].x = wsp[i-1].x + przemieszczenie_x;
        wsp[i].y = wsp[i-1].y +przemieszczenie_y;
    }
    bool search = true;
    wspolrzedne w1, wsr, w2;
    for (int i = 0; i < 100 && search; i++) {
        for (int j = i+1; j < 100 && search; j++) {
            wspolrzedne sr = srodek(wsp[i], wsp[j]);
            for (int k = 0; k < 100 && search; k++) {
                if (wsp[k].x == sr.x && wsp[k].y == sr.y) {
                    search = false;
                    w1 = wsp[i];
                    w2 = wsp[j];
                    wsr = wsp[k];
                }
            }
        }
    }
    cout << "("<< w1.x << " " << w1.y << ") (" << wsr.x << " " << wsr.y << ") (" << w2.x << " " << w2.y << ") ";
    wynik << "("<< w1.x << " " << w1.y << ") (" << wsr.x << " " << wsr.y << ") (" << w2.x << " " << w2.y << ") ";
    plik.close();
    wynik.close();
}

int main() {
    //Zadanie2_1();
    //Zadanie2_2();
    //Zadanie2_3();
    //Zadanie2_4();
    //Zadanie3_1();
    //Zadanie3_2_a();
    //Zadanie3_2_b();
    return 0;

}




