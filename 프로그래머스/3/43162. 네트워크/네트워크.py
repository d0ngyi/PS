visited = set()

def dfs(v,n, computers):
    visited.add(v)
    for i in range(n):
        if computers[v][i] == 1 and i not in visited:
            visited.add(i)
            dfs(i,n, computers)
            


def solution(n, computers):
    answer = 0
    
    for i in range(n):
        if i not in visited:
            dfs(i,n, computers)
            answer += 1
            
    return answer