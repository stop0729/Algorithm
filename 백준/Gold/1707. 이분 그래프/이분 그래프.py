# 이 문제 재미있네

from collections import deque

K = int(input())

for i in range(K):
    V, E = map(int, input().split())

    graph = [[] for i in range(V+1)]


    for j in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (V+1)
    switch = 0

    for j in range(1, V+1):
        q = deque()
        if visited[j] != 0:
            continue
        
        visited[j] = 1
        q.append(j)

        while q:
            next = q.popleft()
            for k in graph[next]:
                if visited[k] == 0:
                    visited[k] = -visited[next]
                    q.append(k)
                elif visited[k] == visited[next]:
                    switch = 1
                    break

    if switch == 0:
        print('YES')
    else:
        print('NO')
        
        