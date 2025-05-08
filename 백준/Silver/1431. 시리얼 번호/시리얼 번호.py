import sys

def num_word(word):
    count = 0
    for i in word:
        if i.isdigit():
            count += int(i)
    return count


n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

arr.sort(key=lambda x:(len(x), num_word(x), x))

for i in arr:
    print(i)