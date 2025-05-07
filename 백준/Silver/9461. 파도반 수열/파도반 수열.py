import sys

t = int(sys.stdin.readline())
dp = [1,1,1,2,2,3,4,5,7,9,12] # len = 12
for _ in range(t):
    n = int(sys.stdin.readline())
    if n > len(dp):
        for i in range(len(dp), n):
            dp.append(dp[i - 2] + dp[i - 3])
        print(dp[-1])
    else:
        print(dp[n - 1])

    
