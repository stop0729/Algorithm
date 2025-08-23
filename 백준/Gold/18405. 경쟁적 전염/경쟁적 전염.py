from collections import deque

n , k = map(int, input().split())

data = []
graph = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            graph.append((data[i][j], 0, i, j))

graph.sort()
q = deque(graph)
target_s, a, b = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx < n and 0<= ny and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
                
print(data[a-1][b-1])