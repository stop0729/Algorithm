C, N = map(int, input().split())

lst = []

for i in range(N):
    cost, customer = map(int, input().split())
    lst.append([cost, customer])

dp = [10**10] * (C+100)
dp[0] = 0

for cost, customer in lst:
    for i in range(customer, C+100):
        dp[i] = min(dp[i-customer] + cost, dp[i])

print(min(dp[C:]))