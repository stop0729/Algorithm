from collections import deque

M, N = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph = []
for i in range(N):
    lst = input()
    graph.append([])
    for j in range(M):
        graph[i].append(int(lst[j]))

q = deque()
q.append([0, 0])
distance = [[10**5]*M for _ in range(N)]
distance[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M:
            if graph[nx][ny] == 0:
                if distance[nx][ny] > distance[x][y]:
                    distance[nx][ny] = distance[x][y]
                    q.append([nx, ny])
            elif graph[nx][ny] == 1:
                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx, ny])

print(distance[N-1][M-1])