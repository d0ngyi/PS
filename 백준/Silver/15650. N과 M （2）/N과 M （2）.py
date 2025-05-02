import sys

def back(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 
    for i in range(start, n + 1):
        if i not in ans:
            ans.append(i)
            back(i)
            ans.pop()



n,m = map(int, sys.stdin.readline().split(" "))

ans = []
back(1)
