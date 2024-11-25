#Written by Arghya Vyas
rounds = int(input())
a = 100
d = 100

for i in range(rounds):
    dice = list(map(int, input().split()))
    if dice[0] > dice[1]:
        d -= max(dice)
    elif dice[0] < dice[1]:
        a -= max(dice)
    else:
        continue

print(a)
print(d)
