import heapq

n = int(input())
m = int(input())

data = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    data[a].append([b, c])

start, end = map(int, input().split())

def dijkstra(start):
    distance = [1e9] * (n+1)
    distance[start] = 0
    q = []

    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in data[now]:
            next, cost = i
            dist_next = cost + dist
            if distance[next] > dist_next:
                distance[next] = dist_next
                heapq.heappush(q, [dist_next, next])

    return distance

distance = dijkstra(start)
print(distance[end])