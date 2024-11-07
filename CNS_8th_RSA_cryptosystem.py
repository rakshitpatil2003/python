import random
from sympy import isprime, nextprime

def generate_prime_candidate(length):
    """ Generate an odd integer randomly. """
    p = random.getrandbits(length)
    return p | (1 << length - 1) | 1  # Ensure it's odd and of the correct bit length

def generate_prime_number(length):
    """ Generate a prime number of a given bit length. """
    p = generate_prime_candidate(length)
    while not isprime(p):
        p = nextprime(p)
    return p

def gcd(a, b):
    """ Compute the greatest common divisor of a and b. """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """ Compute the modular inverse of e mod phi using the Extended Euclidean Algorithm. """
    original_phi = phi
    x0, x1 = 0, 1
    if phi == 1:
        return 0
    while e > 1:
        # q is quotient
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += original_phi
    return x1

def rsa_keygen(bits):
    """ Generate RSA public and private keys. """
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # Common choice for e
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # public_key, private_key

def encrypt(public_key, plaintext):
    """ Encrypt the plaintext using the public key. """
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    """ Decrypt the ciphertext using the private key. """
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example usage
if __name__ == "__main__":
    bits = 8  # Use a small number for demonstration; use at least 1024 bits for security
    public_key, private_key = rsa_keygen(bits)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
