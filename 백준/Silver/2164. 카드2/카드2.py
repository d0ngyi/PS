import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque(list(range(1,n+1)))

while len(queue) != 1:
    queue.popleft()
    k = queue[0]
    queue.popleft()
    queue.append(k)
print(queue[0])