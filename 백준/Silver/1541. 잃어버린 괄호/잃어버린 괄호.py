import sys

word = list(sys.stdin.readline().rstrip().split("-"))


arr =[]

for i in word:
    if "+" not in i:
        arr.append(int(i))
    else:
        num = map(int, i.split("+"))
        arr.append(sum(num))

total = arr[0]

for i in range(1,len(arr)):
    total = total - arr[i]

print(total)
