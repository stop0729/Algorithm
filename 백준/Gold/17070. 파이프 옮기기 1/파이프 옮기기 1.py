from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

data = [list(map(int, input().split())) for i in range(N)]

dp = [[[0] * 3 for i in range(N)] for j in range(N)] # 가로0, 대각선1, 세로2

for i in range(1, N):
    if data[0][i] == 1:
        break
    dp[0][i][0] = 1

for i in range(1, N):
    for j in range(1, N):
        for k in range(3):
            if data[i][j] != 1:
                if k == 0:
                    dp[i][j][k] = dp[i][j-1][1] + dp[i][j-1][0]
                elif k == 1:
                    if data[i-1][j] == 1 or data[i][j-1] == 1:
                        continue
                    dp[i][j][k] = dp[i-1][j-1][1] + dp[i-1][j-1][0] + dp[i-1][j-1][2]
                elif k == 2:
                    dp[i][j][k] = dp[i-1][j][2] + dp[i-1][j][1]

print(sum(dp[N-1][N-1]))