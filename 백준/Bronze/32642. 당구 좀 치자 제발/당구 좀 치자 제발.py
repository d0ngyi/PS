n = int(input())

info = input()
arr = info.split(" ")

for i in range(0, n):
    arr[i] = int(arr[i])

if(arr[0] == 0):
    ans = [-1]
else:
    ans = [1]

for i in range(1, n):
    if(arr[i] == 0):
        ans.append(ans[i - 1] - 1)
    else:
        ans.append(ans[i -1] + 1)

total = 0

for i in range(0, n):
    total += ans[i]

print(total)