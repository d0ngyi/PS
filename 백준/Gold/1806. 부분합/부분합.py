import sys

n,s = map(int, sys.stdin.readline().split(" "))

num = list(map(int, sys.stdin.readline().split(" ")))

left = 0
right = 0
answer = []
sum = num[0]


while left < n:
    # print(num[left:right + 1])
    # print(sum)

    if sum < s:
        if right < n - 1:
            right += 1
            sum += num[right]
        else:
            break
    else: # sum >= s
        answer.append(right - left + 1)
        sum -= num[left]
        left += 1
    






if answer:
    print(min(answer))
else:
    print(0)

# 10 15
# 5 1 3 5 10 7 4 9 2 8