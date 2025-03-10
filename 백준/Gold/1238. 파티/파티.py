import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])


def dijkstra(start):
    distance = [10e9] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue

        for i in graph[node]:
            dist = cost + i[1]
            if dist < distance[i[0]]:
                distance[i[0]] = dist
                heapq.heappush(q, [dist, i[0]])

    return distance

distance = dijkstra(X)

for i in range(1, N+1):
    if i != X:
        distance[i] += dijkstra(i)[X]

print(max(distance[1:]))