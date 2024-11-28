#Written By Arghya Vyas
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#decode algorithm
def decode_letter(encoded_letter, k, position):
    letterc = 26
    encv = letters.index(encoded_letter) + 1
    shift = 3 * position + k
    original = (encv - shift) % letterc
    if original == 0:
        original = letterc
    return letters[original - 1]
k = int(input())
encoded = input()
decoded = ""
for position, letter in enumerate(encoded):
    decodedl = decode_letter(letter, k, position + 1)
    decoded += decodedl

print(decoded)
