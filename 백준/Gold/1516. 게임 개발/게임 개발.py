from collections import deque

N = int(input())

cost = [0] * (N+1)
dp = [0] * (N+1)

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    cost[i] = lst[0]
    for j in range(1, len(lst)):
        if lst[j] == -1:
            break
        else:
            graph[lst[j]].append(i)
            indegree[i] += 1

q = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    dp[now] += cost[now]

    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now])

        if indegree[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(dp[i])