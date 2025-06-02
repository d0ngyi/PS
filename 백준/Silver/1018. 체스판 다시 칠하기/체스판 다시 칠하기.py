import sys

n,m = map(int, sys.stdin.readline().split(" "))

board = []

for i in range(n):
    a = sys.stdin.readline().rstrip()
    board.append(a)
ans = n * m
for i in range(0, n - 7):
    for j in range(0, m - 7):
        count1 = 0
        count2 = 0
        for k in range(i, i + 8):
            for a in range(j, j + 8):
                if (k + a) % 2 == 0:
                    if board[k][a] == "B":
                        count1 += 1
                    if board[k][a] == "W":
                        count2 += 1
                else:
                    if board[k][a] == "W":
                        count1 += 1
                    if board[k][a] == "B":
                        count2 += 1
        ans = min(ans, count1, count2)


print(ans)