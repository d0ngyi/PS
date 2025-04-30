import sys

def binarySearch(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (end + start) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split(" ")))
nList.sort()
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split(" ")))

for i in mList:
    if binarySearch(i, nList):
        print(1)
    else:
        print(0)