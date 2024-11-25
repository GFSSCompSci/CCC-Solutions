#Written By Arghya Vyas
a, b = 0, 0
output = []

def onexn(letter, n):
    global a, b
    if letter == "A":
        a = n
    elif letter == "B":
        b = n

def twox(letter):
    if letter == "A":
        output.append(a)
    elif letter == "B":
        output.append(b)

def threexy(letter):
    global a, b
    if letter == "A":
        a += b
    elif letter == "B":
        b += a

def fourxy(letter):
    global a, b
    if letter == "A":
        a *= b
    elif letter == "B":
        b *= a

def fivexy(letter):
    global a, b
    if letter == "A":
        a -= b
    elif letter == "B":
        b -= a

def sixxy(letter):
    global a, b
    if letter == "A" and b != 0:
        a //= b
    elif letter == "B" and a != 0:
        b //= a

breaker = False
while not breaker:
    command = input().split()
    cmd_type = int(command[0])

    if cmd_type == 1:
        onexn(command[1], int(command[2]))
    elif cmd_type == 2:
        twox(command[1])
    elif cmd_type == 3:
        threexy(command[1])
    elif cmd_type == 4:
        fourxy(command[1])
    elif cmd_type == 5:
        fivexy(command[1])
    elif cmd_type == 6:
        sixxy(command[1])
    elif cmd_type == 7:
        breaker = True

for val in output:
    print(val)
