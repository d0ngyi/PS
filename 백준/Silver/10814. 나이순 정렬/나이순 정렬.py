n = int(input())

arr = []
for i in range(0, n):
    info = input()
    age, name = info.split()
    arr.append([int(age), name])

arr.sort(key=lambda x: x[0])

for i in range(0,n):
    print(arr[i][0], arr[i][1])