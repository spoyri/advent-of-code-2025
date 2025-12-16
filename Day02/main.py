file = open("Day02/input.txt")

list = file.read().split("\n")
list = list[0].split(",")
list = [nums.split("-") for nums in list]

sum = 0

for nums in list:
    start = int(nums[0])
    end = int(nums[1])
    for i in range(start, end+1):
        id = str(i)
        length = len(id)
        if length % 2 == 0 and id[:(length//2)] == id[(length//2):]:
            sum += i

print(sum)
