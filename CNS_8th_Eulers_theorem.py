import re

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
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

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod
    return result

def parse_input(input_str):
    match = re.match(r'(\d+)\*\*(\d+) mod (\d+)', input_str.strip())
    if match:
        a = int(match.group(1))
        b = int(match.group(2))
        m = int(match.group(3))
        return a, b, m
    else:
        raise ValueError("Input must be in the form 'a**b mod m'.")

def compute_modular_exponentiation(input_str):
    a, b, m = parse_input(input_str)
    phi_m = euler_totient(m)
    
    if gcd(a, m) != 1:
        print(f"Since gcd({a}, {m}) != 1, Euler's theorem cannot be directly applied.")
        # Compute directly without reduction
        result = modular_exponentiation(a, b, m)
    else:
        exponent = b % phi_m
        result = modular_exponentiation(a, exponent, m)
    print(f"{a}^{b} mod {m} = {result}")

user_input = input("Enter in the form 'a**b mod m': ")
compute_modular_exponentiation(user_input)
