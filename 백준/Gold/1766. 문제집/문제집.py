import heapq

N, M = map(int, input().split())
answer = []
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
q = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    tmp = heapq.heappop(q)
    answer.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

for i in answer:
    print(i, end = ' ')