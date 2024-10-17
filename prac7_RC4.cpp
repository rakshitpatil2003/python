#include <iostream>
#include <vector>

using namespace std;

// Function to initialize the state array and key-scheduling algorithm (KSA)
void initialize(vector<int>& S, vector<int>& K, vector<int>& key) {
    int j = 0;
    int keyLength = key.size();

    // Initialize S array and key array
    for (int i = 0; i < 8; i++) {
        S[i] = i;
        K[i] = key[i % keyLength];
    }

    // Key-scheduling algorithm (KSA) to scramble S array based on key
    for (int i = 0; i < 8; i++) {
        j = (j + S[i] + K[i]) % 8;
        swap(S[i], S[j]);
    }
}

// Function to generate key stream and encrypt/decrypt the input (RC4 PRGA)
vector<int> rc4_encrypt_decrypt(vector<int> S, vector<int>& plaintext) {
    int i = 0, j = 0;
    vector<int> ciphertext(plaintext.size());

    for (size_t n = 0; n < plaintext.size(); n++) {
        i = (i + 1) % 8;
        j = (j + S[i]) % 8;
        swap(S[i], S[j]);

        // Generate key stream
        int k = S[(S[i] + S[j]) % 8];
        // XOR the plaintext byte with the key stream to get ciphertext
        ciphertext[n] = plaintext[n] ^ k;
    }

    return ciphertext;
}

int main() {
    // Initial State S and Key
    vector<int> S(8), K(8);
    vector<int> key = {5, 1, 0, 1};  // Given key
    vector<int> plaintext = {1, 2, 2, 2};  // Given plaintext (PT)

    // Initialize S and K arrays
    initialize(S, K, key);

    // Encryption
    cout << "Encrypting...\n";
    vector<int> ciphertext = rc4_encrypt_decrypt(S, plaintext);
    cout << "Ciphertext: ";
    for (int c : ciphertext) {
        cout << c << " ";
    }
    cout << endl;

    // Reset the state for decryption (need to reinitialize S)
    initialize(S, K, key);

    // Decryption (same process as encryption for RC4)
    cout << "Decrypting...\n";
    vector<int> decryptedtext = rc4_encrypt_decrypt(S, ciphertext);
    cout << "Decrypted text: ";
    for (int d : decryptedtext) {
        cout << d << " ";
    }
    cout << endl;

    return 0;
}
