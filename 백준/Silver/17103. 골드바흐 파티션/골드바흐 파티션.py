import sys

arr = [True] * 1000001 # True 면 소수
arr[0] = False
arr[1] = False

for i in range(2, len(arr)):
    if arr[i] == True:
        for j in range(i * 2, len(arr), i):
            arr[j] = False


def prime(n):
    count = 0

    for i in range(2,n // 2 + 1):
        if arr[i] and arr[n - i]:
            count += 1
    print(count)



t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    prime(n)


# 5
# 6
# 8
# 10
# 12
# 100