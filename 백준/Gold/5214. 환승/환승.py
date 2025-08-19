import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in temp:
        graph[j].append(N+i+1)

distance = [1e9] * (N+M+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 1
    while(queue):
        next = queue.pop()
        for i in graph[next]:
            if next < N+1:
                if distance[i] > distance[next] + 1:
                    distance[i] = distance[next] + 1
                    queue.append(i)
            else:
                if distance[i] > distance[next]:
                    distance[i] = distance[next]
                    queue.append(i)

bfs(1)
if distance[N] == 1e9:
    print(-1)
else:
    print(distance[N])