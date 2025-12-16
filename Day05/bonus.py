file = open("Day05/input.txt")

input = file.read().split("\n\n")

ranges = input[0].split("\n")

ranges = [[int(id) for id in nums.split("-")] for nums in ranges]

ranges.sort(key=lambda x: x[1]-x[0], reverse=True)
count = 0

for i in range(len(ranges)):
    start = ranges[i][0]
    end = ranges[i][1]
    for j in range(i):
        filterStart = ranges[j][0]
        filterEnd = ranges[j][1]
        if end <= filterEnd and start >= filterStart:
            start = 0
            end = -1
            break
        if end <= filterEnd and end >= filterStart:
            end = filterStart - 1
        if start >= filterStart and start <= filterEnd:
            start = filterEnd + 1
    
    count += end - start + 1
print(count)