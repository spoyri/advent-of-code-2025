file = open("Day02/input.txt")

list = file.read().split("\n")
list = list[0].split(",")
list = [nums.split("-") for nums in list]

sum = 0

def recursiveCheck(base, list, div) :
    if len(list) == 0 : return True
    if base == list[:div]:
        return recursiveCheck(base, list[div:], div)
    return False

def checkForRepetition(id) :
    length = len(id)
    for i in range(2, length+1):
        if length % i == 0 and length > 1:
            div = length // i
            base = id[:div]
            if recursiveCheck(base, id, div):
                return True
    return False

for nums in list:
    start = int(nums[0])
    end = int(nums[1])
    for i in range(start, end+1):
        id = str(i)
        if checkForRepetition(id):
             sum += i
print(sum)
