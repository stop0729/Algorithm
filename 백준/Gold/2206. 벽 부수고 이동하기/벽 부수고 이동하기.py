from collections import deque

n, m = map(int, input().split())

data = []
for i in range(n):
    a = []
    b = list(input())
    for i in range(m):
        a.append(int(b[i]))
    data.append(a)

distance = [[[0]*2 for _ in range(m)] for _ in range(n)]
distance[0][0][0] = 1

q = deque()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q.append([0,0,0])

while q:
    x, y, flag = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < n and 0<= ny < m:
            if data[nx][ny] == 0 and distance[nx][ny][flag] == 0:
                distance[nx][ny][flag] = distance[x][y][flag] + 1
                q.append([nx, ny, flag])
            elif data[nx][ny] == 1 and flag == 0:
                distance[nx][ny][1] = distance[x][y][flag] + 1
                q.append([nx, ny, 1])


result = distance[n-1][m-1]
if min(result) == 0:
    if result[0] == 0 and result[1] == 0:
        print(-1)
    else:
        print(max(result))
else:
    print(min(result))