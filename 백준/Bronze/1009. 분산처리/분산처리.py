import sys

t = int(sys.stdin.readline())



dic = {1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1],0:[10]}

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split(" "))
    if a > 9:
        a = a % 10
    arr = dic[a]
    n = b % len(arr)
    print(arr[n - 1])
