'''def split_word(n_bit_word):
    n = len(n_bit_word)
    left = n_bit_word[:n//2]
    right = n_bit_word[n//2:]
    return left, right

word = input("Enter a binary string: ")

left_half, right_half = split_word(word)
print(f"Left: {left_half}, Right: {right_half}")
'''
'''def swap_halves(n_bit_word):
    n = len(n_bit_word)
    left = n_bit_word[:n//2]
    right = n_bit_word[n//2:]
    return right + left

word = input("Enter a binary string: ")

swapped_word = swap_halves(word)
print(f"Swapped: {swapped_word}")
'''
def apply_pbox(word, pbox):
    return ''.join([word[i] for i in pbox])
word = input("Enter a binary string: ")
pbox = list(map(int, input("Enter permutation box indices separated by spaces: ").split()))
permuted_word = apply_pbox(word, pbox)
print(f"Permuted: {permuted_word}")