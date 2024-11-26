#Written by Arghya Vyas
import math
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

count = 0

cube_root = int(a ** (1 / 3))
if cube_root ** 3 < a:
    cube_root += 1

while True:
    cube = cube_root ** 3
    if cube > b:
        break
    if cube >= a:
        square_root = int(math.sqrt(cube))
        if square_root ** 2 == cube:
            count += 1
    cube_root += 1

# Output the result
print(count)
