# By: Kevin Xia
# Solution: Brute force every possibility

def solve(aString, bString, integer_sequence, num_element_limit):
    if aString == bString and len(aString) > 0:
        return integer_sequence
    if len(integer_sequence) < num_element_limit:
        for idx in range(len(a_elements)):
            newSequence = integer_sequence[:]
            newSequence.append(idx)
            result = solve(aString + a_elements[idx], bString + b_elements[idx], newSequence, num_element_limit)
            if result is not None:
                return result
    return None # if we didn't get a valid sequence

limit = int(input())
n = int(input())
a_elements = []
b_elements = []
for _ in range(n):
    a_elements.append(input())
for _ in range(n):
    b_elements.append(input())
    
ans = solve("", "", [], limit)
if ans is None:
    print("No solution.")
else:
    print(len(ans))
    for num in ans:
        print(num + 1) # since it's 0-indexed