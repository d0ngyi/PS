import sys

word = list(sys.stdin.readline().rstrip().upper())

dic = {}

for i in word:
    if i not in dic:
        dic[i] = word.count(i)

max = 0
same = False
for i in dic:
    if dic[i] > max:
        max = dic[i]
        ans = i
        same = False
    elif dic[i] == max:
        same = True

if same:
    print("?")
else:
    print(ans)


