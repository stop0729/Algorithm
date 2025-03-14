import heapq

N, E = map(int, input().split())

data = [[] for i in range(N+1)]

for i in range(E):
    start, end, cost = map(int, input().split())
    data[start].append([end, cost])
    data[end].append([start, cost])




def dijkstra(start):
    q = []
    distances = [1e9] * (N+1)
    distances[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        if dist > distances[now]:
            continue

        for i in data[now]:
            end, cost = i
            if dist+cost < distances[end]:
                distances[end] = dist + cost
                heapq.heappush(q, [dist+cost, end])

    return distances

start, end = map(int, input().split())
distances1 = dijkstra(1)
temp1 = distances1[start] # 1 - 2
temp2 = distances1[end] # 1 - 3
d1_N = distances1[N] # 1 - 4
distances_start = dijkstra(start)
temp3 = distances_start[end] # 2 - 3
temp6 = distances_start[N] # 2 - 4
distances_end = dijkstra(end)
temp4 = distances_end[N] # 3 - 4
temp5 = distances_end[start] # 3 - 2
result = min(temp1+temp4, temp2+temp6, temp1+d1_N+temp2) + temp5


if result >= 1e9:
    print(-1)
else:
    print(result)

# 1 - 2 - 3 - 4
# 1 - 3 - 2 - 4
# 1 - 2 - 3 - 1 - 4
# 1 - 3 - 2 - 1 - 4