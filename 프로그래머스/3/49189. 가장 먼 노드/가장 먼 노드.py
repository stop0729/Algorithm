import heapq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for i in edge:
        a, b = i
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    inf = int(1e9)
    distance = [inf] * (n+1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    answer = 0
    tmp = max(distance[1:])
    for i in distance:
        if i == tmp:
            answer += 1
    return answer