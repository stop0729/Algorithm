N = int(input())

data = [list(map(int, input().split())) for i in range(N)]

dp1 = data[0]
dp2 = data[0]

for i in range(1, N):

    dp1 = [data[i][0] + max(dp1[0], dp1[1]), data[i][1] + max(dp1[0], dp1[1], dp1[2]), data[i][2] + max(dp1[1], dp1[2])]
    dp2 = [data[i][0] + min(dp2[0], dp2[1]), data[i][1] + min(dp2[0], dp2[1], dp2[2]), data[i][2] + min(dp2[1], dp2[2])]

print(max(dp1), min(dp2))