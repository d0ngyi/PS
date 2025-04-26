import sys

n = int(sys.stdin.readline())
dance = set(["ChongChong"])

for i in range(0, n):
    p1, p2 = sys.stdin.readline().split()
    if p1 in dance:
        dance.add(p2)
    elif p2 in dance:
        dance.add(p1)

print(len(dance))
