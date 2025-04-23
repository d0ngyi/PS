n = int(input())

arr = set()
for i in range(0,n):
    name,log = input().split(" ")
    if(log == "enter"):
        arr.add(name)
    else:
        arr.remove(name)


for name in sorted(arr, reverse=True):
    print(name)

