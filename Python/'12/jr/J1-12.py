#Written By Arghya Vyas
l = int(input())
s = int(input())

if s <= l:
    print("Congratulations, you are within the speed limit!")
elif s > l:
    if s - l <= 20:
        print("You are speeding and your fine is $100.")
    elif s - l <= 30:
        print("You are speeding and your fine is $270.")
    elif s - l >= 31:
        print("You are speeding and your fine is $500.")