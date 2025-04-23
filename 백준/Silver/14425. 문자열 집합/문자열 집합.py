n,m = (input()).split(" ")

n = int(n)
m = int(m)

nArr = []
mArr = []

for i in range(0, n):
    nArr.append(input())

for i in range(0, m):
    mArr.append(input())

total = 0

for i in range(0, m): #mArr
    if(mArr[i] in nArr):
        total += 1


print(total)