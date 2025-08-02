import sys

n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split(" "))
m = int(sys.stdin.readline())
graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

#print(graph)

visited = set()
answer = -1
def dfs(node, target, depth):
    global answer
    if node == target:
        answer = depth
        return
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, target, depth + 1)

dfs(a, b, 0)
print(answer)