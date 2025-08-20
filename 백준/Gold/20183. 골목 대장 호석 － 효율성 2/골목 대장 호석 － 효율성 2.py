import sys
import heapq

input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) # a에서 b로 가는데 cost 만큼
    graph[b].append((a, cost))


# 경로의 지불값의 최대값들중 최소를 구하는중.
# 판별하기 위해서는 경로에서 나오는 값들이 우리가 정한 최소값보다 크면 못 지나가게 조건을 걸고,
# 그것을 만족하는 거리가 있으면 true. 즉 solution은 최소값을 찾는중이네


# r>=l로 두면  r = mid-1로 둬도 됨. 이때 r은 범위를 좁히는 용도이므로 mid가 답
# r>l로 두면 r = mid로 두어야 함
# 아래처럼 하면 마지막으로 true였던 mid가 ans가 되는것
def solution():
    l = 0
    r = 10**18
    while (r>=l):
        mid = (l + r) // 2 
        if get_rout(mid):
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return -1 if r == 10**18 else ans

# 



def get_rout(mid):
    distance = [10**18] * (N+1)
    distance[A] = 0

    q = []
    heapq.heappush(q, (0, A))

    while q:
        dist, cur  = heapq.heappop(q)

        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            next, cost = i
            if cost > mid:
                continue
            next_dist = cost + dist
            if next_dist < distance[next]:
                distance[next] = next_dist
                heapq.heappush(q, (next_dist, next))

    if distance[B] == 10**18 or distance[B] > C:
        return False
    else:
        return True
    
result = solution()
print(result)