#Written By Arghya Vyas
trout = int(input())
pike = int(input())
pickerel = int(input())
maxp = int(input())
count = 0

for trout_count in range(maxp // trout + 1):
    for pike_count in range(maxp //pike + 1):
        for pickerel_count in range(maxp // pickerel + 1):
            total = (trout_count * trout +
                            pike_count *
                            pike +
                            pickerel_count * pickerel)
            if 0 < total <= maxp:
                print(trout_count, "Brown Trout,", pike_count, "Northern Pike,", pickerel_count, "Yellow Pickerel")
                count += 1
print(f'Number of ways to catch fish: {count}')
