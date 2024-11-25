#Written By Arghya Vyas
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

if d1 == d2 == d3 ==d4:
    print("Fish At Constant Depth")
elif d1 < d2 < d3 < d4:
    print("Fish Rising")
elif d1 > d2 > d3 > d4:
    print("Fish Diving")
else:
    print("No Fish")