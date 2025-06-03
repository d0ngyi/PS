import sys


def prime(n):
    arr = [1] * (2 * n + 1) # 1 이면 소수
    arr[0] = 0
    arr[1] = 0

    for i in range(1,len(arr)):
        if arr[i] == 1:
            for j in range(i * 2,len(arr),i):
                arr[j] = 0

    count = 0
    for i in range(n + 1,len(arr)):
        if arr[i] == 1:
            count += 1
    print(count)


while 1:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    prime(n)


