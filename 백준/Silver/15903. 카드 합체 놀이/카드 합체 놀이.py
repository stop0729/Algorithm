import heapq

n, m = map(int, input().split())

lst = list(map(int, input().split()))
q = []

for i in range(len(lst)):
    heapq.heappush(q, lst[i])

for i in range(m):
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    heapq.heappush(q, first+second)
    heapq.heappush(q, first+second)

print(sum(q))