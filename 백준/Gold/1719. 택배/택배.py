import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

result = [["-"]*(n+1) for _ in range(n+1)]


def dikstra(start):
    q = []
    distances = [10**10] * (n+1)
    distances[start] = 0
    route = [0]*(n+1)

    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if dist > distances[now]:
            continue

        for i in graph[now]:
            next_node, next_cost = i
            next_dist = dist + next_cost
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                route[next_node] = now
                heapq.heappush(q, [next_dist, next_node])

    for i in range(1, n+1):
        if i == start:
            continue

        now = i

        while result[start][i] == "-":
            if route[now] == start:
                result[start][i] = now
            else:
                now = route[now]

for i in range(1, n+1):
    dikstra(i)

for i in range(1, n+1):
    print(*result[i][1:])