file = open("Day06/input.txt")
lines = file.read().splitlines()

equations = []
i = 0
equation = []
while i < len(lines[0]):
    if lines[4][i] != " ":
        equation = []
        equations.append(equation)
        equation.append(lines[4][i])
        num = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        equation.append(int(num))
    else:
        num = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
        if num != "    ":
            equation.append(int(num))
    i += 1

sum = 0
for equation in equations:
    if equation[0] == "*":
        result = 1
        for j in range(1, len(equation)):
            result *= equation[j]
    else:
        result = 0
        for j in range(1, len(equation)):
            result += equation[j]
    sum += result

print(sum)