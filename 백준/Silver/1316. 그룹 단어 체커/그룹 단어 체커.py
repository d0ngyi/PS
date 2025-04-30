import sys

n = int(sys.stdin.readline())
count = 0
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    check = []
    prevAlp = word[0]
    a = True
    for i in word:
        if i in check and prevAlp != i:
            a = False
            break
        check.append(i)
        prevAlp = i
    if a:
        count += 1
print(count)
