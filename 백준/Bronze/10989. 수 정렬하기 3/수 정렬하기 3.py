import sys

n = int(sys.stdin.readline())

numList = [0] * 100001

for i in range(0, n):
    num = int(sys.stdin.readline().rstrip())
    numList[num] += 1
#print("=" * 10)
for i in range(1, 10001):
    if numList[i] != 0:
        for j in range(0, numList[i]):
            print(i)