def swap_halves(n_bit_word):
    n = len(n_bit_word)
    left = n_bit_word[:n//2]
    right = n_bit_word[n//2:]
    return right + left

word = input("Enter a binary string: ")

swapped_word = swap_halves(word)
print(f"Swapped: {swapped_word}")