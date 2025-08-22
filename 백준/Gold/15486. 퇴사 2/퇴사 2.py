n = int(input())

data = [0] * (n+2)

for i in range(1, n+1):
    t, p = map(int, input().split())
    data[i] = max(data[i-1], data[i])
    if i+t <= n+1:
        data[t+i] = max(data[t+i], data[i] + p)

data[n+1] = max(data[n+1], data[n])
print(data[n+1])