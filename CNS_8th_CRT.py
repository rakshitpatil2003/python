def extended_gcd(a, b):
    """ Extended Euclidean Algorithm to find the GCD and the coefficients. """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """ Function to find the modular inverse of a under modulo m. """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} under modulo {m}.")
    else:
        return x % m

def chinese_remainder_theorem(a_list, m_list):
    """ Solve the system of congruences using the Chinese Remainder Theorem. """
    if len(a_list) != len(m_list):
        raise ValueError("Lists a and m must be of the same length.")
    
    total = 0
    prod = 1
    
    for m in m_list:
        prod *= m
    
    for a, m in zip(a_list, m_list):
        partial_prod = prod // m
        inv = mod_inverse(partial_prod, m)
        total += a * partial_prod * inv
    
    return total % prod, prod

# Main function
if __name__ == "__main__":
    n = int(input("Enter the number of inputs: "))
    
    a_list = []
    m_list = []
    
    for _ in range(n):
        a, m = map(int, input("Enter a and m in the format 'a m': ").split())
        a_list.append(a)
        m_list.append(m)

    result, prod = chinese_remainder_theorem(a_list, m_list)
    print(f"The solution to the system of congruences is: x ≡ {result} (mod {prod})")
