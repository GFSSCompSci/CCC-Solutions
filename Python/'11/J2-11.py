#Written By Arghya Vyas
h = int(input())
m = int(input())
n = 1
def alt(t):
    global h, m
    alt = -6*(t**4) + h*(t**3) + 2*(t**2) + t
    return alt

while True:
    t = alt(n)
    if n > m or n > 240:
        print('The balloon does not touch ground in the given time.')
        break
    if t > 0:
        n +=1
        continue
    elif t <= 0:
        print('The balloon first touches ground at hour:')
        print(n)
        break
    if n > m or n > 240:
        print('The balloon does not touch ground in the given time.')
        break