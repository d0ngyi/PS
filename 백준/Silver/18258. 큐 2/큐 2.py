import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(0, n):
    info = info = sys.stdin.readline().split()
    if info[0] == "push":
        queue.append(int(info[1]))
    elif info[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
            queue.popleft()
    elif info[0] == "size":
        print(len(queue))
    elif info[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif info[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[- 1])