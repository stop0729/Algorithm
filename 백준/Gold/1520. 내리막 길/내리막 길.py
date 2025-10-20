import sys
sys.setrecursionlimit(10**5)

m, n = map(int, input().split())

graph = []

for i in range(m):
    lst = list(map(int, input().split()))
    graph.append(lst)

dp = [[-1] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0<= ny < n:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0,0))