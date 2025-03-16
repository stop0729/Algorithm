N = int(input())

data = list(map(int, input().split()))
data2 = data[::-1]

dp1 = [1] * N
dp3 = [1] * N

lst1 = []
for i in range(N):
    for j in range(i):
        if data[i] > data[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if data2[i] > data2[j]:
            dp3[i] = max(dp3[i], dp3[j]+1)

result = 0
dp3.reverse()

for i in range(N):
    if dp1[i] + dp3[i] > result:
        result = dp1[i] + dp3[i]

print(result - 1)


# 뒤집어서 증가하는 수열 = 감소하는 수열
# 감소하는 수열 dp 결과를 뒤집은거 != 뒤집어서 증가하는 수열의 dp
