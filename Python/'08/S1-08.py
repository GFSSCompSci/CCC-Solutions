data = []
n = input().split()
data.append((n[0], int(n[1])))
while "Waterloo" not in n[0]:
    n = input().split()
    data.append((n[0], int(n[1])))
data.sort(key=lambda x: x[1])
print(data[0][0])
