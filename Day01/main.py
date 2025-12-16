file = open("Day01/input.txt")

list = file.read().split("\n")[:-1]
list = [(inst[0], int(inst[1:])) for inst in list]

point = 50
count = 0

for i in list:
    move = i[1]
    count += move // 100
    move = move % 100
    if i[0] == "L":
        count -= (point == 0)
        point = (point - move)
    else:
        point = (point + move)
    if move > 0:
        count += (point <= 0 or point >= 100)
    point = point % 100

print(count)