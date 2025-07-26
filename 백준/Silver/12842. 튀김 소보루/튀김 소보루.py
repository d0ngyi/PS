import sys

n, s = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

time = [int(sys.stdin.readline()) for _ in range(m)]
time_count = [t - 1 for t in time]

answer = 0

while n > s:

    remain_times = [time[i] - time_count[i] for i in range(m)]
    min_time = min(remain_times)


    for i in range(m):
        time_count[i] += min_time


    for i in range(m):
        if time_count[i] == time[i]:
            time_count[i] = 0
            n -= 1
            answer = i + 1
            if n == s:
                break

print(answer)
