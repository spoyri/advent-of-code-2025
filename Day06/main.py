file = open("Day06/input.txt")
lines = file.read().splitlines()
lines = [line.split(" ") for line in lines]
lines = [list(filter(lambda x: x != '', line)) for line in lines]

sum = 0
for i in range(len(lines[0])):
    if lines[4][i] == "*":
        sum += int(lines[0][i]) * int(lines[1][i]) * int(lines[2][i]) * int(lines[3][i])
    else:
        sum += int(lines[0][i]) + int(lines[1][i]) + int(lines[2][i]) + int(lines[3][i])

print(sum)