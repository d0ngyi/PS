import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(0, n):
    info = list(map(int, sys.stdin.readline().split(" ")))
    if info[0] == 1:
        queue.appendleft(info[1])
    elif info[0] == 2:
        queue.append(info[1])
    elif info[0] == 3:
        if len(queue) > 0:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif info[0] == 4:
        if len(queue) > 0:
            print(queue[-1])
            queue.pop()
        else:
            print(-1)
    elif info[0] == 5:
        print(len(queue))
    elif info[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif info[0] == 7:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)