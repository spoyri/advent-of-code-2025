import math

file = open("Day08/input.txt")
lines = file.read().splitlines()
lines = [[int(num) for num in line.split(",")] for line in lines]

distances = []

groups = [[0]]
lines[0].append(0)

for i in range(1, len(lines)):
    groups.append([i])
    lines[i].append(i)
    cord1 = lines[i]
    for j in range(i):
        cord2 = lines[j]
        distance = math.sqrt(math.pow(cord1[0] - cord2[0], 2) + math.pow(cord1[1] - cord2[1], 2) + math.pow(cord1[2] - cord2[2], 2))
        distances.append([i, j, distance])

distances.sort(key=lambda x: x[2])


for i in range(1000):
    distance = distances[i]
    cord1 = lines[distance[0]]
    cord2 = lines[distance[1]]
    print(f"Connecting indexes {distance[0]} and {distance[1]}")
    if cord1[3] != cord2[3]:
        newGroup = groups[cord1[3]].extend(groups[cord2[3]])
        groups[cord2[3]] = []
        groupIndex = cord1[3]
        for index in groups[cord1[3]]:
            lines[index][3] = groupIndex
    else:
        print("Already connected!")
groups.sort(key=lambda x: len(x), reverse=True)
print(groups)
sum = 0
for i in groups:
    sum += len(i)
print(sum)
print(len(groups[0]) * len(groups[1]) * len(groups[2]))