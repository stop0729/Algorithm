N = int(input())

data = list(map(int, input().split()))

dp = [0] * (N)
dp[0] = data[0]

for i in range(N):
    for j in range(i):
        if data[i] > data[j]:
            if dp[j] == 0:
                dp[j] = data[j]
            dp[i] = max(dp[i], dp[j]+data[i])

print(max(dp))