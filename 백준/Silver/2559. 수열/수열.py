import sys

n, k = map(int, sys.stdin.readline().split(" "))

temp = list(map(int, sys.stdin.readline().split(" ")))

ans = sum(temp[:k])
maxSum = ans

for i in range(k, n):
    ans = ans - temp[i - k] + temp[i]
    maxSum = max(maxSum, ans)

print(maxSum)