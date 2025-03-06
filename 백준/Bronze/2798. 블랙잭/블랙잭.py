N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            com = data[i] + data[j] + data[k]
            if  com<= M and com > result:
                result = com

print(result)