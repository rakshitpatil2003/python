def split_word(n_bit_word):
    n = len(n_bit_word)
    left = n_bit_word[:n//2]
    right = n_bit_word[n//2:]
    return left, right

word = input("Enter a binary string: ")

left_half, right_half = split_word(word)
print(f"Left: {left_half}, Right: {right_half}")