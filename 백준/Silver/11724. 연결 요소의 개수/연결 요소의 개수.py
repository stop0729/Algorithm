N, M = map(int, input().split())

data = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [0] * (N+1)
    
def dfs(data, start, visited):
    out = data[start]
    for i in out:
        if visited[i] != 1:
            visited[i] = 1
            dfs(data, i, visited)


result = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(data, i, visited)
        result += 1

print(result)