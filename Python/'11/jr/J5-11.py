#Written by Arghya Vyas
def dfs(graph, node):
    if not graph[node]: 
        return 1 
    count = 1 
    for child in graph[node]:
        count *= (dfs(graph, child) + 1)
    return count

n = int(input())
graph = {i: [] for i in range(1, n+1)}

for i in range(1, n):
    invite = int(input())
    graph[invite].append(i)

start = n
print(dfs(graph, start))