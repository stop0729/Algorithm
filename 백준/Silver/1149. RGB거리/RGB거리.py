N = int(input())

data = []
dp = [[10e9] * 3 for _ in range(N)]

for i in range(N):
    data.append(list(map(int, input().split())))

dp[0] = data[0]
for i in range(1, N):
    for j in range(3): # 현재 줄
        for k in range(3): # 이전 줄
            if j != k:
                dp[i][j] = min(dp[i-1][k] + data[i][j], dp[i][j])

print(min(dp[i]))