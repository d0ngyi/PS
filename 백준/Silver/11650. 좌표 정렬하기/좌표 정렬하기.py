import sys

n = int(sys.stdin.readline().rstrip())

coordinate = []

for i in range(0, n):
    x, y = map(int, sys.stdin.readline().split(" "))
    coordinate.append([x, y])

coordinate.sort()

for i in range(0, n):
    print(coordinate[i][0], coordinate[i][1])
