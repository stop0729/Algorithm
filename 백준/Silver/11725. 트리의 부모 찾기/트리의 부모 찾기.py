import heapq
from collections import deque

N = int(input())

data = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [0] * (N+1)
visited[1] = 1
q = deque()

# def dfs(start):
#     out = data[start]
#     for i in out:
#         if visited[i] == 0:
#             visited[i] = start
#             dfs(i)
#     return

# dfs(1)

def bfs(start):
    q.append(start)
    while q:
        out = q.popleft()
        for i in data[out]:
            if visited[i] == 0:
                visited[i] = out
                q.append(i)

bfs(1)

for i in range(2, N+1):
    print(visited[i])