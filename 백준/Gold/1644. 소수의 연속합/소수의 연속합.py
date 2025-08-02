import sys

def prime(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    m = int((n + 1) ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve

n = int(sys.stdin.readline())
sieve = prime(n)

num = []

for i in range(2,n + 1):
    if sieve[i]:
        num.append(i)



count = 0
left = 0
right = 0
sum = 0

while True:
    if sum >= n:
        if sum == n:
            count += 1
        sum -= num[left]
        left += 1
    elif right == len(num):
        break
    else:
        sum += num[right]
        right += 1

print(count)
    

