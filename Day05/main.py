file = open("Day05/input.txt")

input = file.read().split("\n\n")

ranges = input[0].split("\n")
ids = input[1].split("\n")[:-1]

ranges = [[int(id) for id in nums.split("-")] for nums in ranges]

count = 0

for i in ids:
    id = int(i)
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            count += 1
            break

print(count)