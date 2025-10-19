from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    lst = []
    tmp = input()
    for j in range(len(tmp)):
        lst.append(int(tmp[j]))
    graph.append(lst)

Q = int(input())
house = []
for i in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    house.append([(x1, y1), (x2, y2)])

visited = [[1] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = 0
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    q.append([nx, ny])

bfs(0, 0)

cumul = [[0]*(M+1) for _ in range(N+1)]


# padding 해서 누적합 구하는게 중요하네
for i in range(1, N):
    for j in range(1, M):
        cumul[i][j] = cumul[i-1][j] + cumul[i][j-1] + visited[i][j] - cumul[i-1][j-1]

for i in range(Q):
    left_up, right_down = house[i]
    x1, y1 = left_up
    x2, y2 = right_down
    tmp = cumul[x2-1][y2-1] - cumul[x1-1-1][y2-1] - cumul[x2-1][y1-1-1] + cumul[x1-2][y1-2]
    if tmp == 0:
        print("Yes")
    else:
        print("No", tmp)