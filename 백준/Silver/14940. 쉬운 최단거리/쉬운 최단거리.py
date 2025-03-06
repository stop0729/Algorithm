from collections import deque

n, m = map(int, input().split())

data = [list(map(int, input().split())) for i in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            q.append((i, j))
            data[i][j] = 0
        if data[i][j] == 1:
            data[i][j] = -1
            
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def bfs(data):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and data[nx][ny] == -1:
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))
                
bfs(data)

for i in range(n):
    for j in range(m):
        print(data[i][j], end= ' ')
    print()