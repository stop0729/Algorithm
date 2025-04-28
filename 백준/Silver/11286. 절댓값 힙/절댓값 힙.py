import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(q) == 0:
            print(0)
        else:
            t = heapq.heappop(q)
            print(t[1])
    else:
        heapq.heappush(q, (abs(temp), temp))