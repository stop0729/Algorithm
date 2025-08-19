import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0] # 북 동 서 남
dy = [0, 1, 0, -1]

def change_dir(d, i): # 반시계
    d = d-i
    if d<0:
        d += 4
    return d

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

result = 0
while(True):
    if graph[r][c] == 0:
        graph[r][c] = -1
        result += 1
    else:
        switch = 0 # 4방향 확인하면서 청소 안된곳 있는지 확인
        for _ in range(4):
            d = change_dir(d, 1)
            nx = r + dx[d]
            ny = c + dy[d]
            if (0<=nx<N and 0<=ny<M and graph[nx][ny] == 0):
                switch = 1
                r = nx
                c = ny
                break

        if switch == 0: # 4방향 다 청소 되어있음
            nx = r - dx[d]
            ny = c - dy[d]
            if (0<=nx<N and 0<=ny<M and graph[nx][ny]!= 1):
                r = nx
                c = ny
            else:
                break

print(result)