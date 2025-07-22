import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split(" ")))
b,c = map(int,sys.stdin.readline().split(" "))

total_num = 0

for i in a:
    count = 1
    i = i - b
    if i > 0:
        if i % c > 0:
            count += i // c + 1
        else:
            count += i // c
    total_num += count

print(total_num)
