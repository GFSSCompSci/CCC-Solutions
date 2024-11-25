# By: Kevin Xia
import sys

input = sys.stdin.readline # unnecessary but works

n = int(input()) # getting inputs
connections = dict()

for i in range(1, n + 1):
    connections[str(i)] = [] # setting up each possible value to be a list of previous nodes
    
while True: # begin adding the connections
    x, y = input().split()
    if x == '0' and y == '0':
        break
    connections[y].append(x)
    
waysToReach = {'1' : 1,} # begin calculating the ways to reach each number
for num in range(2, n + 1):
    waysToReach[str(num)] = 0
    for connected in connections[str(num)]:
        waysToReach[str(num)] += waysToReach[connected] # get the ways to reach each number based on its previous connections
print(waysToReach[str(n)]) # print our result