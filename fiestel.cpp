#include <iostream>
using namespace std;

int F(int R, int key) {
    return R ^ key;
}

void feistelRound(int &L, int &R, int key) {
    int new_L = R;
    int new_R = L ^ F(R, key);
    L = new_L;
    R = new_R;
}

void feistelCipher(int &L, int &R, int key1, int key2) {
    feistelRound(L, R, key1);
    feistelRound(L, R, key2);
}

int main() {
    int L, R;
    int key1 = 25;
    int key2 = 50; 

    cout << "Enter the left half (L): ";
    cin >> L;
    cout << "Enter the right half (R): ";
    cin >> R;
    cout << "Original L: " << L << " R: " << R << endl;

    feistelCipher(L, R, key1, key2);
    cout << "After Feistel Cipher (two rounds): L: " << L << " R: " << R << endl;

    return 0;
}