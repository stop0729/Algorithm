n = int(input())

data = [0] * (1002)

data[0] = 0
data[1] = 1
data[2] = 2

for i in range(3, n+1):
    data[i] = data[i-1] + data[i-2]

data[n] = data[n] % 10007
print(data[n])