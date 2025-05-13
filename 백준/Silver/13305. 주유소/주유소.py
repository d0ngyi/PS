import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split(" ")))
price = list(map(int, sys.stdin.readline().split(" ")))
ans = 0

a = 0

while a != n:
    oilPrice = price[a]
    point = price[a]
    for j in range(a + 1, n - 1):
        if oilPrice > price[j]:
            point = j
            break
    if point == price[a]:
        ans = ans + sum(distance[a:]) * oilPrice
        break
    else:
        ans = ans + sum(distance[a:point]) * oilPrice
    
    a += point


print(ans)