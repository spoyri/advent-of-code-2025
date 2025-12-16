file = open("Day04/input.txt")
lines = file.read().split("\n")[:-1]
spotCount = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "@":
            count = 0
            for j in range(-1, 2):
                for i in range(-1, 2):
                    y2 = y + j
                    x2 = x + i
                    if (y2 >= 0 and y2 < len(lines) 
                        and x2 >= 0 and x2 < len(lines[y]) 
                        and (y2 != y or x2 != x) 
                        and lines[y2][x2]== "@"):
                        count += 1
            if count < 4:
                spotCount += 1

print(spotCount)