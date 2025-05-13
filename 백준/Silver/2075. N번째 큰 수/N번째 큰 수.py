import heapq

N = int(input())

q = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in temp: 
        if len(q) < N:
            heapq.heappush(q, j)
        else:
            if q[0] < j:
                heapq.heappop(q)
                heapq.heappush(q, j)

answer = heapq.heappop(q)
print(answer)