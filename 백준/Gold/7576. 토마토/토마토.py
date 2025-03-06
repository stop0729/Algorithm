from collections import deque

M, N = map(int, input().split())

data = []
q = deque()
all_ripe = True

for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)
    for j in range(M):
        if temp[j] == 1:
            q.append([i, j])
        elif temp[j] == 0:
            all_ripe = False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < M and 0<= ny < N :
                if data[ny][nx] == 0:
                    data[ny][nx] = data[y][x] + 1
                    q.append([ny, nx])
                
bfs()
result = 0
cant_ripe = False 

for i in range(N):
    for j in range(M):
        if data[i][j] > result:
            result = data[i][j]
        if data[i][j] == 0:
            cant_ripe = True
            
if all_ripe == True:
    print(0)
elif cant_ripe == True:
    print(-1)
else:
    print(result-1)