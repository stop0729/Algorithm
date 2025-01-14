N = int(input())
process = []
dp = [0] * (N+1)
dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])

while N != 1:
    process.append(N)
    temp = N-1
    if N % 2 == 0: 
        if dp[temp] > dp[N//2]:
            temp = N//2
    if N % 3 == 0:
        if dp[temp] > dp[N//3]:
            temp = N//3
    N = temp

process.append(1)

for i in range(len(process)):
    print(process[i], end = ' ')