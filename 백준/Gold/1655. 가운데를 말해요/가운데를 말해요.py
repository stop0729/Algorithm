import heapq
import sys
input = sys.stdin.readline

n = int(input())

left = []
right = []

for i in range(n):
    temp = int(input())

    if len(left) == 0 or temp <= -left[0]:
        heapq.heappush(left, -temp)
    else:
        heapq.heappush(right, temp)


    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])
