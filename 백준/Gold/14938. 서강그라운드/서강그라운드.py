import heapq

n, m, r = map(int, input().split())

item = list(map(int, input().split()))
item = [0] + item

graph = [[] for i in range(n+1)]
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distances = [0] * (n+1)

def dijkstra(start):
    distances = [1e9] * (n+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            new_node, cost = i
            if cost + dist < distances[new_node]:
                distances[new_node] = cost + dist
                heapq.heappush(q, [cost+dist, new_node])
    
    return distances


result = 0
for i in range(1, n+1):
    distances = dijkstra(i)
    temp = 0
    for j in range(len(distances)):
        if distances[j] <= m:
            temp += item[j]
    
    if result < temp:
        result = temp

print(result)