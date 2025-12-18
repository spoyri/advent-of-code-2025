file = open("Day03/input.txt")

lines = file.read().split("\n")[:-1]

sum = 0

def recursiveListCheck(index: int, value: int, result: list[int]) -> None:
    if index > 11:
        return
    elif value >= result[index]:
        temp = result[index]
        result[index] = value
        recursiveListCheck(index+1, temp, result)


result = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
    for i in range(len(line)-1, -1, -1):
        num = int(line[i])
        if i >= len(line)-12:
            result[i - len(line)] = num
        else:
            recursiveListCheck(0, num, result)
    resultNum = ""
    for i in result:
        resultNum += str(i)
    sum += int(resultNum)

print(sum)