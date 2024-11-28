#Written By Arghya Vyas
mined = [
    [0, -1], [0, -2], [0, -3], [0, -4], [1, -3], [2, -3],
    [3, -3], [3, -4], [3, -5], [4, -5], [5, -5],
    [5, -4], [5, -3], [6, -3], [7, -3], [7, -4],
    [7, -5], [7, -6], [7, -7], [6, -7], [5, -7],
    [4, -7], [3, -7], [2, -7], [1, -7], [0, -7],
    [-1, -7], [-1, -6], [-1, -5]
]

start = [-1, -5]

while True:
    i = input().split(' ')
    direction = i[0]
    steps = int(i[1])
    status = 'safe'

    if direction == 'q':
        break

    initial_position = start.copy()

    while steps > 0:
        if direction == 'l':
            start[0] -= 1
        elif direction == 'r':
            start[0] += 1
        elif direction == 'u':
            start[1] += 1
        elif direction == 'd':
            start[1] -= 1
        steps -= 1


        if start in mined:
            status = 'DANGER'


        mined.append(start.copy())


    if status == 'DANGER':
        print(start[0], start[1], status)
        break
    else:
        print(start[0], start[1], status)
