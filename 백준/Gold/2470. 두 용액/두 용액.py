import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split(" ")))

num.sort()

left = 0
right = n - 1

answer = [num[0], num[1]]

while left < right:
    if abs(sum(answer)) > abs(num[left] + num[right]):
        answer = [num[left], num[right]]

    if num[left] + num[right] == 0:
        answer = [num[left], num[right]]
        break
    elif num[left] + num[right] < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])