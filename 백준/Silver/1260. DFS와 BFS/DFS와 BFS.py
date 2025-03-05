from collections import deque

N, M, V = map(int, input().split())
data = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(len(data)):
    data[i].sort()

    
def dfs(data, start, visited):
    out = data[start]
    for i in out:
        if visited[i] != 1:
            visited[i] = 1
            print(i, end=' ')
            dfs(data, i, visited)
            
def bfs(data, start, visited):
    q = deque([start])
    visited[start] = 1
    print(start, end=' ')
    while q:
        out = q.popleft()
        for i in data[out]:
            if visited[i] != 1:
                visited[i] = 1
                print(i, end= ' ')
                q.append(i)


start = V
visited = [0] * (N+1)
visited[start] = 1
print(start, end=' ')
dfs(data, start, visited)
print()

visited = [0] * (N+1)
bfs(data, start, visited)