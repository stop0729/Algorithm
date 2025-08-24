def dfs(n, start, data, visited):
    for i in data[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(n, i, data, visited)
    
def solution(n, computers):
    data = [[] for i in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                data[i+1].append(j+1)
 
                
    visited = [False] * (n+1)
    answer = 0
    
    for start in range(1, n+1):
        if visited[start] == False:
            visited[start] = True
            answer += 1
            dfs(n, start, data, visited)
            
    return answer