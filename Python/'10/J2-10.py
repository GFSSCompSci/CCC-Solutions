#Written By Arghya Vyas
a = int(input()) 
b = int(input()) 
c = int(input()) 
d = int(input()) 
s = int(input()) 


nikky_cycle = a + b
byron_cycle = c + d


nikky_full_cycles = s // nikky_cycle
nikky_remaining_steps = s % nikky_cycle
Nikky = nikky_full_cycles * (a - b) + min(nikky_remaining_steps, a)


byron_full_cycles = s // byron_cycle
byron_remaining_steps = s % byron_cycle
Byron = byron_full_cycles * (c - d) + min(byron_remaining_steps, c)


if Byron > Nikky:
    print("Byron")
elif Nikky > Byron:
    print("Nikky")
else:
    print("Tied")
