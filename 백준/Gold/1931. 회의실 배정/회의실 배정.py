N = int(input())

data = []
for i in range(N):
    start, end = map(int, input().split())
    data.append([start,end])

data = sorted(data, key = lambda x : (x[1], x[0]))

start, end = data[0]
result = 1

for i in range(1, len(data)):
    new_start, new_end = data[i]
    if new_start >= end:
        start, end = data[i]
        result += 1

print(result)