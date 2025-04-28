import sys

n = int(sys.stdin.readline())

time = []

for i in range(0, n):
    start, end = map(int, sys.stdin.readline().split())
    time.append((start, end))

sortedTime = sorted(time, key=lambda x:(x[1], x[0]))

count = 1
endTime = sortedTime[0][1]

for i in range(1, n):
    if sortedTime[i][0] >= endTime:
        endTime = sortedTime[i][1]
        count += 1

print(count)