#Written By Arghya Vyas
def back(time):   
    if time < 0:
        time += 2400
    return time

def mintohour(time):
    hours = time // 100
    minutes = time % 100
    if minutes >= 60:
        hours += minutes // 60  
        minutes = minutes % 60  
    
    return hours * 100 + minutes

ottawa = int(input())

victoria = back(ottawa - 300)  
edmonton = back(ottawa - 200)  
winnipeg = back(ottawa - 100)  
toronto = ottawa
halifax = back(ottawa + 100)  
stjohns = back(mintohour(ottawa + 130))   

print(f'{ottawa} in Ottawa')
print(f'{victoria} in Victoria')
print(f'{edmonton} in Edmonton')
print(f'{winnipeg} in Winnipeg')
print(f'{ottawa} in Toronto')
print(f'{halifax} in Halifax')
print(f"{stjohns} in St. John's")
