import sys

n = int(sys.stdin.readline())

answer = 0

for i in range(1,n + 1):
    if i < 100:
        answer += 1
        continue
    
    arr = list(map(int, str(i)))

    if arr[0] - arr[1] == arr[1] - arr[2]:
        answer += 1


print(answer)