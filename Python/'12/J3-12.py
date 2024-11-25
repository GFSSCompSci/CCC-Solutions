#Written By Arghya Vyas
line1 = ['*', 'x', "*"]
line2 = [" ", "x", 'x']
line3 = ['*', ' ','*']
k = int(input())
top = [x*k for x in line1]
mid = [x*k for x in line2]
bottom = [x*k for x in line3]
for i in range(k):
    print(''.join(top))
for i in range(k):
    print(''.join(mid))
for i in range(k):
    print(''.join(bottom))
