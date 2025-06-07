import sys

n,m = map(int, sys.stdin.readline().split(" "))

dic = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

sortedDic = dict(sorted(dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for i in sortedDic:
    print(i)