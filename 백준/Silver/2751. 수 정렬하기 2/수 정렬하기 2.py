import heapq

h = []
n = int(input())

for i in range(n):
    heapq.heappush(h, int(input()))
   

for i in range(n):
    a = heapq.heappop(h)
    print(a)