# DOES NOT WORK YET
#Written By Arghya Vyas
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]
w = int(input())

cline = []
clen = 0

for word in words:
    if clen + len(word) + len(cline) <= w:
        cline.append(word)
        clen += len(word)
    else:
        spaces_needed = w - clen
        if len(cline) > 1:
            even_spaces = spaces_needed // (len(cline) - 1)
            extra_spaces = spaces_needed % (len(cline) - 1)

            line = ""
            for i in range(len(cline) - 1):
                line += cline[i]
                line += "." * (even_spaces + (1 if i < extra_spaces else 0))
            line += cline[-1]
        else:
            line = cline[0] + "." * spaces_needed

        print(line)
        cline = [word]
        clen = len(word)

if cline:
    line = ".".join(cline)
    line += "." * (w - len(line))
    print(line)

