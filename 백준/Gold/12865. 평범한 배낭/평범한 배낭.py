N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
data = []
for i in range(N):
    data.append(list(map(int, input().split())))


for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= data[i-1][0]:
            dp[i][j] = max(data[i-1][1] + dp[i-1][j-data[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])