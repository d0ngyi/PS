import sys

n, m = map(int, sys.stdin.readline().split(" "))

notListen = set()
notSee = set()

for _ in range(n):
    notListen.add(sys.stdin.readline().rstrip())

for _ in range(m):
    notSee.add(sys.stdin.readline().rstrip())

ans = []
count = 0

for i in notListen:
    if i in notSee:
        ans.append(i)
        count += 1

ans.sort()

print(count)
for i in ans:
    print(i)
