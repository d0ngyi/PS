import sys

n = int(sys.stdin.readline())

wordList = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in wordList:
        wordList.append(word)

wordList.sort(key=lambda word:(len(word), word))

for i in wordList:
    print(i)