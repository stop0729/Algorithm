T = int(input())

for i in range(T):
    n = int(input())
    data = []
    data1 = list(map(int, input().split()))
    data2 = list(map(int, input().split()))
    for i1, i2 in zip(data1, data2):
         data.append([i1, i2])

    dp = [[0]*2 for i in range(n+1)]
    dp[1] = data[0]
    for j in range(2, n+1):
         dp[j][0] = max(dp[j-1][1], dp[j-2][0], dp[j-2][1]) + data[j-1][0]
         dp[j][1] = max(dp[j-1][0], dp[j-2][0], dp[j-2][1]) + data[j-1][1]

    print(max(dp[n]))