def gcd(a, b):
    """ Compute the greatest common divisor of a and b. """
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """ Extended Euclidean Algorithm to find the GCD and coefficients. """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse_fermat(a, p):
    """ Calculate the modular inverse using Fermat's Little Theorem. """
    if gcd(a, p) != 1:
        raise ValueError(f"{a} and {p} are not coprime, so inverse does not exist.")
    
    # Fermat's theorem: a^(p-1) ≡ 1 (mod p) => a^(p-2) ≡ a^(-1) (mod p)
    inv = pow(a, p - 2, p)
    print(f"Using Fermat's theorem: a^({p}-2) mod {p} = {inv}")
    return inv

def euler_totient(n):
    """ Calculate Euler's Totient Function φ(n). """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def mod_inverse_euler(a, m):
    """ Calculate the modular inverse using Euler's Totient Theorem. """
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime, so inverse does not exist.")
    
    phi_m = euler_totient(m)
    inv = mod_inverse_fermat(a, phi_m)  # Use Fermat's method with φ(m)
    print(f"Using Euler's theorem: a^({phi_m}-1) mod {m} = {inv}")
    return inv

def main():
    print("Choose a method to calculate the modular inverse:")
    print("1. Fermat's Little Theorem")
    print("2. Euler's Totient Theorem")
    
    choice = input("Enter 1 or 2: ")
    
    a = int(input("Enter the value of 'a': "))
    m = int(input("Enter the value of 'm': "))

    if choice == '1':
        try:
            result = mod_inverse_fermat(a, m)
            print(f"The modular inverse of {a} mod {m} is: {result}")
        except ValueError as e:
            print(e)
    elif choice == '2':
        try:
            result = mod_inverse_euler(a, m)
            print(f"The modular inverse of {a} mod {m} is: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
