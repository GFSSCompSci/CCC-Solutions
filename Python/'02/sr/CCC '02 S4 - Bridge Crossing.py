# By: Kevin Xia
# Solution: Dynamic programming

m = int(input())
n = int(input())
people_info = [(-1, -1)] + [(input(), int(input())) for _ in range(n)] # 1-indexed for simplicity

prev = [0] * (n + 1) # Tracks the split point for each person to form the optimal groupings
dp = [0] * (n + 1) # `dp[i]` stores the minimum time required for the first i people

for i in range(1, n + 1):
    best = float('inf')
    
    for j in range(max(1, i - m + 1), i + 1): # try every group size ending at the current person while keeping constraints in mind
        time = max(people_info[j:i + 1], key = lambda x: x[1])[1] + dp[j - 1] # current time is determined by the maximum time in this group, plus the time to process all previous tasks
        if time < best: # Update the best time and the split point if this grouping is better
            best = time
            prev[i] = j - 1 # record the end of the previous group

    dp[i] = best
    
# reconstructing the groupings
cur = n
res = []
while cur != 0:
    group = [] 
    for i in range(prev[cur] + 1, cur + 1):
        group.append(people_info[i][0])

    res.append(group.copy())
    cur = prev[cur]

print(f"Total Time: {dp[-1]}")
for i in reversed(res): # Output the groupings in reverse order (since they were constructed in reverse)
    print(" ".join(i))