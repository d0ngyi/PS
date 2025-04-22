n = int(input())

for i in range(0,n):
    info = input()
    arr = list(info)

    for j in range(0, int(len(arr) / 2)):
        for k in range(0, len(arr) - 1):
            try:
                if(arr[k] == "(" and arr[k + 1] == ")"):
                    del arr[k]
                    del arr[k]
            except IndexError:
                break

    if(len(arr) == 0):
        print("YES")
    else:
        print("NO")
