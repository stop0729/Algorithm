import sys

input = sys.stdin.readline

n = int(input())
graph = [[1e9] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0 

while(True):
    a, b = map(int, input().split())
    if a != -1:
        graph[a][b] = 1
        graph[b][a] = 1
    else:
        break

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

compare = []
for i in range(1, n+1):
    max = 0
    for j in range(1, n+1):
        if graph[i][j] > max:
            max = graph[i][j]
    compare.append(max)

score = min(compare)
result = []
for i in range(len(compare)):
    if compare[i] == score:
        result.append(i+1)

print(score, len(result))
for i in range(len(result)):
    print(result[i], end = ' ')