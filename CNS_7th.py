def rc4(key, plaintext):
    """ RC4 encryption and decryption function. """
    # Key Scheduling Algorithm (KSA)
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap
        K = S[(S[i] + S[j]) % 256]
        ciphertext.append(chr(ord(char) ^ K))  # XOR

    return ''.join(ciphertext)

def main():
    print("RC4 Encryption and Decryption")
    
    key = input("Enter the encryption key: ").encode()  # Convert key to bytes
    plaintext = input("Enter the plaintext: ")

    # Encrypt the plaintext
    ciphertext = rc4(key, plaintext)
    print(f"Ciphertext (encrypted): {''.join(['{:02x}'.format(ord(c)) for c in ciphertext])}")

    # Decrypt the ciphertext
    decrypted_text = rc4(key, ciphertext)
    print(f"Decrypted plaintext: {decrypted_text}")

if __name__ == "__main__":
    main()
