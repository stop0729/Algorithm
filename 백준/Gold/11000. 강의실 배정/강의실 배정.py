import heapq

n = int(input())

t = []
for i in range(n):
    a, b = map(int, input().split())
    t.append((a,b))

t.sort(key = lambda x : x[0])

q = []
result = 1
q.append(t[0][1])

for i in range(1, n):
    while q:
        temp = heapq.heappop(q)
        if t[i][0] < temp:
            heapq.heappush(q, temp)
            heapq.heappush(q, t[i][1])
            break
    else:
        heapq.heappush(q, t[i][1])
    if len(q) > result:
        result = len(q)

print(result)