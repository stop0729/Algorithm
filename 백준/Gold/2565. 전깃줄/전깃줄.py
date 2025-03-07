N = int(input())

data = []
for i in range(N):
    a, b = map(int, input().split())
    data.append([a, b])

data.sort(key = lambda x : x[0])

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if data[i][1] > data[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N - max(dp))