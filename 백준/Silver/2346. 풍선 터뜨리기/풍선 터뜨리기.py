import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque(range(1, n + 1))
num = list(map(int, sys.stdin.readline().split())) #3 2 1 -3 -1

ans = []
ans.append(queue[0])
queue.popleft()
paper = num[0]

for i in range(0 , n - 1):
    if paper > 0 :
        queue.rotate(-paper + 1)
        ans.append(queue[0])
        paper = num[queue[0] - 1]
        queue.popleft()
    else:
        queue.rotate(-paper)
        ans.append(queue[0])
        paper = num[queue[0] - 1]
        queue.popleft()

for i in ans:
    print(i, end=" ")