from collections import deque

def bfs(a, graph, n):
    visited = [0] * (n+1)
    visited[a] = 1
    q = deque()
    q.append(a)
    ans = 1
    
    while q:
        next = q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                ans += 1

    return ans
                
        

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for i in wires:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)
    
    answer = n
    for i in wires:
        a, b = i
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a, graph, n) - bfs(b, graph, n)), answer)

        graph[a].append(b)
        graph[b].append(a)
    
    return answer