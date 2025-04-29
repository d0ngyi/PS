import sys

word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

ans = []

for i in range(len(word)):
    ans.append(word[i])
    if ''.join(ans[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            ans.pop()


if not ans:
    print("FRULA")
else:
    print("".join(ans))