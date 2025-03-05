import sys
from collections import deque

M, N, T = map(int, input().split())
q = deque([])

data = []
for i in range(T):
    data_N = []
    for j in range(N):
        data_N.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if data_N[j][k] == 1:
                q.append([i, j, k])
    data.append(data_N)

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            n_z, n_y, n_x = z+dz[i], y+dy[i], x+dx[i]
            if 0<= n_z <T and 0<= n_y < N and 0<= n_x < M and data[n_z][n_y][n_x] == 0:
                data[n_z][n_y][n_x] = data[z][y][x] + 1
                q.append([n_z, n_y, n_x])

bfs()

flag = False
result = 0
for i in range(T):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 0:
                flag = True
                break
            if data[i][j][k] > result:
                result = data[i][j][k]

if flag == True:
    print(-1)
else:
    print(result-1)
    


# 1. 어떻게 bfs 이동하고 어떻게 횟수 계산? 어디서 부터 어떻게 시작? -> 처음 1인것들 전부 큐에 넣고 시작
# 2. 어떻게 익지 않은 토마토를 판별? -> 다 마친후 0이 있는지를 판별... 괜히 어렵게 생각했네