#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
// Zadanie 3

// Zadanie 3.1
int shortcut(int key) {
    int result = 0;
    int stopien = 1;
    while (key > 0) {
        int cyfra = key % 10;
        key /= 10;
        if (cyfra % 2 != 0) {
            result += cyfra * stopien;
            stopien *= 10;
        }
    }
    return result;
}

string z3_path_skrot_txt = "../zalaczniki-2024/skrot.txt";
// Zadanie 3.2
void Zadanie3_2() {
    ifstream plik(z3_path_skrot_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z3_path_skrot_txt << endl;
    }
    ofstream wynik("wynik3_2.txt");
    int liczba;
    int max = -1;
    int liczba_nieistniejacych = 0;
    while (plik >> liczba) {
        if (shortcut(liczba) == 0) {
            liczba_nieistniejacych ++;
            if (liczba > max) {
                max = liczba;
            }
        }
    }
    cout << liczba_nieistniejacych << endl;
    cout << max << endl;
    wynik << liczba_nieistniejacych << endl;
    wynik << max << endl;

    wynik.close();
    plik.close();
}

string z3_path_skrot2_txt = "../zalaczniki-2024/skrot2_przyklad.txt";
// Zadanie 3.3
// sito euklidesa - https://www.matemaks.pl/najwiekszy-wspolny-dzielnik-nwd.html
int nwd(int a, int b){
    while (b != 0) {
        int pom = b;
        b = a % b;
        a = pom;
    }
    return a;
}


void Zadanie3_3() {
    ifstream plik(z3_path_skrot2_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z3_path_skrot2_txt << endl;
    }
    ofstream wynik("wynik3_3.txt");

    int liczba;
    while (plik >> liczba) {
        int skrot = shortcut(liczba);
        if (nwd(liczba, skrot) == 7) {
            cout << liczba << endl;
            wynik << liczba << endl;
        }
    }

    wynik.close();
    plik.close();
}


// Zadanie 4

//Zadanie 4.1
string z4_path_liczby_txt = "../zalaczniki-2024/liczby.txt";

bool jest_dzielnikiem(int pierwsza, vector<int> tablica) {
    for (int liczba : tablica) {
        if (liczba % pierwsza == 0) {
            return true;
        }
    }
    return false;
}

void Zadanie4_1() {
    ifstream plik(z4_path_liczby_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z4_path_liczby_txt << endl;
    }
    ofstream wynik("wynik4_1.txt");
    vector<int> liczba_pierwsza;
    vector<int> liczba_calkowita;
    for (int i =0; i<3000 ;i ++) {
        int pierwsza;
        plik >> pierwsza;
        liczba_pierwsza.push_back(pierwsza);
    }
    for (int i =0; i<20 ;i ++) {
        int liczba;
        plik >> liczba;
        liczba_calkowita.push_back(liczba);
    }
    int licznik = 0;
    for (int pierwsza : liczba_pierwsza) {
        if (jest_dzielnikiem(pierwsza, liczba_calkowita)) {
            licznik++;
        }
    }
    cout << licznik << endl;
    wynik << licznik << endl;
    wynik.close();
    plik.close();
}

// Zadanie 4.2
bool wiekszy(int a, int b) {
    return a > b;
}

void Zadanie4_2() {
    ifstream plik(z4_path_liczby_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z4_path_liczby_txt << endl;
    }
    ofstream wynik("wynik4_2.txt");
    vector<int> liczba_pierwsza;
    vector<int> liczba_calkowita;
    for (int i =0; i<3000 ;i ++) {
        int pierwsza;
        plik >> pierwsza;
        liczba_pierwsza.push_back(pierwsza);
    }
    for (int i =0; i<20 ;i ++) {
        int liczba;
        plik >> liczba;
        liczba_calkowita.push_back(liczba);
    }
    sort(liczba_pierwsza.begin(), liczba_pierwsza.end(), wiekszy);
    cout << liczba_pierwsza[100] << endl;
    wynik << liczba_pierwsza[100] << endl;
    wynik.close();
    plik.close();
}


// Zadanie 4.3
void Zadanie4_3() {
    ifstream plik(z4_path_liczby_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z4_path_liczby_txt << endl;
    }
    ofstream wynik("wynik4_3.txt");
    vector<int> liczba_pierwsza;
    vector<int> liczba_calkowita;
    for (int i =0; i<3000 ;i ++) {
        int pierwsza;
        plik >> pierwsza;
        liczba_pierwsza.push_back(pierwsza);
    }
    for (int i =0; i<20 ;i ++) {
        int liczba;
        plik >> liczba;
        liczba_calkowita.push_back(liczba);
    }
    sort(liczba_pierwsza.begin(), liczba_pierwsza.end(), wiekszy);
    for (int liczba : liczba_calkowita) {
        int sprawdzana = liczba;
        for (int pierwsza : liczba_pierwsza) {
            if (sprawdzana % pierwsza == 0) {
                sprawdzana /= pierwsza;
            }
        }
        if (sprawdzana == 1) {
            cout << liczba << endl;
            wynik << liczba << endl;
        }

    }
    wynik.close();
    plik.close();
}

// Zadanie 4.4
void Zadanie4_4() {
    ifstream plik(z4_path_liczby_txt);
    if (!plik.is_open()) {
        cerr << "Can't open file " << z4_path_liczby_txt << endl;
    }
    ofstream wynik("wynik4_4.txt");
    vector<int> liczba_pierwsza;
    vector<int> liczba_calkowita;
    for (int i =0; i<3000 ;i ++) {
        int pierwsza;
        plik >> pierwsza;
        liczba_pierwsza.push_back(pierwsza);
    }
    for (int i =0; i<20 ;i ++) {
        int liczba;
        plik >> liczba;
        liczba_calkowita.push_back(liczba);
    }

    vector<int> kumulowana;
    int suma = 0;
    for (int pierwsza: liczba_pierwsza) {
        kumulowana.push_back(suma);
        suma += pierwsza;
    }

    int size = 50;
    float max_srednia = -1;
    int r_max, l_max;
    for (int r=0; r < 3000 - size; r++) {
        for (int l=r+size; l < 3000-1; l++) {
            float sum = kumulowana[l+1] - kumulowana[r];
            float srednia = sum / (l-r+1);
            if (max_srednia < srednia) {
                max_srednia = srednia;
                r_max = r;
                l_max = l;
            }
        }
    }
    cout << max_srednia << " " << l_max - r_max + 1 << " " << liczba_pierwsza[r_max] << endl;
    wynik.close();
    plik.close();
}


int main() {
    Zadanie3_2();
    Zadanie3_3();
    Zadanie4_1();
    Zadanie4_2();
    Zadanie4_3();
    Zadanie4_4();
    return 0;
}