import sys

n,m = map(int, sys.stdin.readline().split())

pokemonNum = {}
pokemonName = {}

for i in range(0, n):
    name = sys.stdin.readline().rstrip()
    pokemonNum[i + 1] = name
    pokemonName[name] = i + 1


for i in range(0 ,m):
    q = sys.stdin.readline().rstrip()

    if q.isdigit():
        print(pokemonNum[int(q)])
    else:
        print(pokemonName[q])