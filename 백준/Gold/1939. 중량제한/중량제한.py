from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
bridges = [[] for _ in range(n+1)]

for i in range(m):
	a,b,c = map(int,input().split())
	bridges[a].append([b,c])
	bridges[b].append([a,c])
      
a, b = map(int, input().split())

def bfs(weight):
    q = deque()
    q.append(a)
    visited = [False] * (n+1)
    visited[a] = True

    while q:
          now = q.popleft()

          for next, w in bridges[now]:
                if not visited[next] and w >= weight:
                        visited[next] = True
                        q.append(next)

    if visited[b]: return True
    else: return False

start = 0
end = 1000000000
result = 0

while start <= end:
    mid = (start+end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)