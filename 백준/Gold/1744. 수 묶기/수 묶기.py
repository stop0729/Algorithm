N = int(input())

data = []

for i in range(N):
    temp = int(input())
    data.append(temp)

plus = []
minus = []
result = 0

for i in range(N):
    if data[i] > 1:
        plus.append(data[i])
    elif data[i] <= 0:
        minus.append(data[i])
    else:
        result += data[i]

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)