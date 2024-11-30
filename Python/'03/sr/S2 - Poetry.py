# By: Kevin Xia
# Basic implementation
def find_last(word):
    word = word.strip().lower()
    for i in range(len(word) - 1, 0, -1):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == ' ': # getting the last syllable as defined by the problem
            return word[i:]
    return word

n = int(input())

for i in range(n):
    last_syllables = []
    for i in range(4):
        last_syllables.append(find_last(input()))
    
    if last_syllables[0] == last_syllables[1] == last_syllables[2] == last_syllables[3]:
        print("perfect")
    elif last_syllables[0] == last_syllables[1] and last_syllables[2] == last_syllables[3]:
        print("even")
    elif last_syllables[0] == last_syllables[2] and last_syllables[1] == last_syllables[3]:
        print("cross")
    elif last_syllables[0] == last_syllables[3] and last_syllables[1] == last_syllables[2]:
        print("shell")
    else:
        print("free")