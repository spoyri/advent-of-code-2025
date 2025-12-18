file = open("Day03/input.txt")

lines = file.read().split("\n")[:-1]

sum = 0

for line in lines:
    first = 0
    second = 0
    for i in line:
        num = int(i)
        if second > first:
            first = second
            second = num
        elif num > second:
            second = num
    sum += first*10 + second

print(sum)
