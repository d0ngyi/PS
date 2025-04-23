recur = 0

def fib(n):
    global recur
    if(n == 1 or n == 2):
        recur += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())

dp = n - 2
a = fib(n)

print(recur, dp)