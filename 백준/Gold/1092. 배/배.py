import sys

n = int(sys.stdin.readline())
crane_limit = list(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
box_weight = list(map(int, sys.stdin.readline().split(" ")))

crane_limit.sort(reverse = True)
box_weight.sort(reverse = True)

# print(crane_limit)
# print(box_weight)

answer = 0

if crane_limit[0] < box_weight[0]:
    print(-1)
    sys.exit()


while len(box_weight) > 0:
    for i in range(n):
        for j in range(len(box_weight)):
            if crane_limit[i] >= box_weight[j]:
                box_weight.pop(j)
                break
    answer += 1

print(answer)