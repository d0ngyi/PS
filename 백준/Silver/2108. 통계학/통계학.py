import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

dic = {}

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

sortedDic = (sorted(dic.items(), key=lambda item : -item[1]))

print(round(sum(arr) / len(arr))) #산술평균
print(arr[int(len(arr) / 2)]) #중앙값
if len(sortedDic) > 1 and sortedDic[0][1] == sortedDic[1][1]:
    print(sortedDic[1][0])
else:
    print(sortedDic[0][0])
print(max(arr) - min(arr)) #범위