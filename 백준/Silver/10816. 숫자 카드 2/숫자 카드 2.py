import sys

n = int(sys.stdin.readline())
nCard = sorted(list(map(int, sys.stdin.readline().split(" "))))
m = int(sys.stdin.readline())
mCard = list(map(int, sys.stdin.readline().split(" ")))

dic = {}

for i in nCard:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in mCard:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end= " ")