import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(q) == 0:
            print('0')
        else:
            result = heapq.heappop(q)
            print(str(result[1]))
    else:
        heapq.heappush(q, [-temp, temp])