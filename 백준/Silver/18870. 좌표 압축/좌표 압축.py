import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split(" ")))
arr2 = sorted(set(arr))

dic = {}

for i in range(len(arr2)):
    dic[arr2[i]] = i

for i in arr:
    print(dic[i], end=" ")