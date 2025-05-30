import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))
dp = [[0] * 3 for _ in range(n)]

dp[0] = arr[0]


for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + arr[i][2]
print(min(dp[n -1]))