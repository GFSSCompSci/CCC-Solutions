#Written By Arghya Vyas
breaker = 0
listWrap = []
counter = {}
cycles = 0

while breaker != 1:
    e = []  
    n = list(map(int, input().split()))  

    if n[0] == 0: 
        breaker = 1
        print(listWrap)  
        print(counter)  
        print(cycles) 
    else:
       
        for ints in range(0, len(n) - 1):
            a = abs(n[ints] - n[ints + 1])
            if n[ints] > n[ints + 1]:
                a = a * -1 
            e.append(a)

       
        e.sort()
        listWrap.append(e)  

      
        for count in e:
            if count in counter:
                counter[count] += 1
            else:
                counter[count] = 1
      
        seen = set() 
        for value in counter.values():
            if value > 1: 
                cycles += 1  