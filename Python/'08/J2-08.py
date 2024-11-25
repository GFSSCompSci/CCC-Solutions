playlist = ["A", 'B', 'C', 'D', "E"]
breaker = 0
while breaker==0:
    button = int(input())
    n = int(input())
    for i in range(n):
        if button == 1:
            playlist.append(playlist[0])
            playlist.pop(0)
        elif button == 2:
            playlist.insert(0, playlist[4])
            playlist.pop(5)
        elif button == 3:
            playlist.insert(0, playlist[1])
            playlist.pop(2)
        elif button == 4:
            print(playlist[0], playlist[1], playlist[2], playlist[3], playlist[4])
            breaker +=1
            