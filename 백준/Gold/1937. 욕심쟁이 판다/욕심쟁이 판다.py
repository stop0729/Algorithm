import sys
sys.setrecursionlimit(10**5)

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dp = [[0]*n for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx < n and 0<=ny < n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]
    
answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)