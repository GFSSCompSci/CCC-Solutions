#Written By Arghya Vyas
from collections import deque

def knight_minimum_moves():
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    start = tuple(map(int, input("").split()))
    end = tuple(map(int, input("").split()))

 
    start_x, start_y = start
    end_x, end_y = end
    

    if start == end:
        return 0
    
    # BFS
    queue = deque([(start_x, start_y, 0)]) 
    visited = set()  
    visited.add((start_x, start_y))
    
    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            

            if 1 <= new_x <= 8 and 1 <= new_y <= 8:

                if (new_x, new_y) == (end_x, end_y):
                    return moves + 1
                

                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, moves + 1))
    
    return -1


print(knight_minimum_moves())
