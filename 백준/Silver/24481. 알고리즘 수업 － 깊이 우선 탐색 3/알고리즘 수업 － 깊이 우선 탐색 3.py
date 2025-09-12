import sys

sys.setrecursionlimit(10**5)

N, M, R = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [-1] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()
    
def dfs(R, distance):
    visited[R] = distance
    for i in graph[R]:
        if visited[i] == -1:
            dfs(i, distance+1)
            
dfs(R, 0)
for i in range(1, len(visited)):
    print(visited[i])