N = int(input())

M = int(input())

graph = [[0]*(N+1)  for i in range(N+1)]

for i in range(1, N+1):
    graph[i][1:N] = list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] !=0 and graph[k][j] !=0:
                graph[i][j] = graph[i][k] + graph[k][j]
              
travel = list(map(int, input().split()))

switch = 0
for i in range(len(travel)-1):
    a, b = travel[i], travel[i+1]
    if graph[a][b] == 0:
        switch = 1



if switch == 1:
    print('NO')
else:
    print('YES')