import sys

def back():
    if len(ans) == m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1, n + 1):
        ans.append(i)
        back()
        ans.pop()


n,m = map(int, sys.stdin.readline().split(" "))

ans = []
back()
