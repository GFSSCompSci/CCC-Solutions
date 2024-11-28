#Written By Arghya Vyas
t1 = int(input())  
t2 = int(input())  
counter = 2  


while t1 >= t2:
    new = t1 - t2  
    t1, t2 = t2, new  
    counter += 1 


print(counter)  
