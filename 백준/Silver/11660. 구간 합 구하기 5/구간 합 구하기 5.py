import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []
for i in range(1, N+1):
    data.append(list(map(int, input().split())))

# coordinate = []
# for i in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = 0

#     for j in range(x1-1, x2):
#         result += sum(data[j][y1-1:y2])

#     print(result)

dp = [[0] * (N+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = data[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
