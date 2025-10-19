from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    q = deque()
    q.append([a,b])


    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif graph[nx][ny] ==1 :
                    visited[nx][ny] += 1

time = 0

while True:
    visited = [[0] * M for _ in range(N)]
    
    bfs(0, 0)
    time += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                graph[i][j] = 0

    air_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                air_cnt += 1
    
    if air_cnt == N*M:
        break

print(time)