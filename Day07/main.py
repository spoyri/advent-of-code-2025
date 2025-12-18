file = open("Day07/input.txt")
lines = file.read().splitlines()

splitters = []

def recursiveSplitters(x: int, y: int) -> None:
    while y < len(lines):
        if lines[y][x] == "^":
            if y * 1000 + x not in splitters:
                recursiveSplitters(x-1, y)
                recursiveSplitters(x+1, y)
                splitters.append(y * 1000 + x)
            return
        y += 1

for i in range(len(lines[0])):
    if lines[0][i] == "S":
        recursiveSplitters(i, 1)

print(len(splitters))
