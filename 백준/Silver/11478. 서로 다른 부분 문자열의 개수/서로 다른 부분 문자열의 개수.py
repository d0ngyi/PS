import sys

word = list(sys.stdin.readline().rstrip())

ans = set()

for i in range(1, len(word) + 1):
    for j in range(0, len(word) - i + 1):
        ans.add(''.join(word[j:i + j]))

print(len(ans))