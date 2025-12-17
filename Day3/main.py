file = open("input.txt")

lines = file.read().split("\n")[:-1]

for line in lines:
    for i in line:
        