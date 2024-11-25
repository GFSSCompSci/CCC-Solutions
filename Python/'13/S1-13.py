#Written by Arghya Vyas
year = int(input())

while True:
    year += 1
    year_str = str(year)
    if len(set(year_str)) == len(year_str):
        print(year)
        break
