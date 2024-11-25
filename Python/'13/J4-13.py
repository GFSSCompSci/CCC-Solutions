#Written By Arghya Vyas
time_available = int(input())
num_chores = int(input())
chores = []

for c in range(num_chores):
    chore_time = int(input())
    chores.append(chore_time)
chores.sort()


total_time = 0
count = 0

for time in chores:
    if total_time + time <= time_available:
        total_time += time  
        count += 1        
    else:
        break 


print(count)
