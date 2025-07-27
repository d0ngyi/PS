import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split(" ")))
num.sort()
x = int(sys.stdin.readline())


count = 0

left = 0
right = n - 1

while left < right:
    if num[left] + num[right] == x:
        count += 1
        left += 1
        right -= 1
    elif num[left] + num[right] < x:
        left += 1
    else:
        right -= 1

print(count)
