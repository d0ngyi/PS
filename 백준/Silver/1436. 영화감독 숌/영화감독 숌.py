import sys

n = int(sys.stdin.readline())

count = 0
num = 666
while 1:
    if "666" in str(num):
        count += 1

    if count == n:
        break
    num += 1

print(num)