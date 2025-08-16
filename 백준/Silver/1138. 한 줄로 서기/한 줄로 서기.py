import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

answer = [n + 1] * n

for i in range(n):
    count = 0
    for j in range(n):
        if count == arr[i] and answer[j] == n + 1:
            answer[j] = i + 1
            break
        if answer[j] > i + 1:
            count += 1
        

for i in answer:
    print(i, end=" ")