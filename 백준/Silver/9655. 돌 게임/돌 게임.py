import sys

n = int(sys.stdin.readline())

count = 0
ans = 0
while n != count:
    ans += 1
    if count + 1 == n:
        count += 1
        continue
    if count + 3 == n:
        count += 3
        continue

    count += 1

if count % 2 == 1:
    print("SK")
else:
    print("CY")

