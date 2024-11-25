#Arghya Vyas
vn = int(input())
votes = input()
a = votes.count("A")
b = votes.count("B")
if a > b:
    print("A")
elif b > a:
    print("B")
elif a == b:
    print("Tie")
