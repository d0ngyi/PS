import sys

n,k = map(int, sys.stdin.readline().split(" "))
arr = list(map(str, sys.stdin.readline().rstrip()))

for i in range(n):
    if arr[i] == 'P':
        start = max(0, i - k)
        end = min(n - 1,i + k)
        for j in range(start, end + 1):
            if arr[j] == 'H':
                arr[j] = "E"
                break


print(arr.count("E"))