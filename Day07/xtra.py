file = open("Day07/input.txt")
lines = file.read().splitlines()

splitters = {}

def recursiveSplitters(x: int, y: int) -> None:
    while y < len(lines):
        if lines[y][x] == "^":
            if y * 1000 + x not in splitters:
                left = recursiveSplitters(x-1, y)
                right = recursiveSplitters(x+1, y)
                splitters[y * 1000 + x] = left + right
                return left + right
            else:
                return splitters[y * 1000 + x]
        y += 1
    return 1

for i in range(len(lines[0])):
    if lines[0][i] == "S":
        print(recursiveSplitters(i, 1))
