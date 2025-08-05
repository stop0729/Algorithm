N = int(input())
dp = [0] * (N + 1)
s = [0] * (N + 1)

for i in range(1, N + 1):
    s[i] = int(input())

if N == 1:
    print(s[1])
elif N == 2:
    print(s[1] + s[2])
else:
    dp[1], dp[2], dp[3] = s[1], s[2], s[3]

    for i in range(4, N + 1):
        dp[i] = min(dp[i - 2], dp[i - 3]) + s[i]

    print(sum(s) - min(dp[N - 1], dp[N - 2]))