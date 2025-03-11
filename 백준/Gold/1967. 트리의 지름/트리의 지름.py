import sys
import heapq

inf = 1e9
n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    distance = [inf] * (n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[1:]

result = 0
distance = dijkstra(1)
temp = max(distance)
temp = distance.index(temp)
result = max(dijkstra(temp+1))

print(result)
