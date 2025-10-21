import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n)
switch = 0

def dfs(start, cnt):
    global switch
    if cnt >= 5:
        switch = 1
        return
    
    if switch == 1:
        return

    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


for i in range(n):
    dfs(i, 0)

if switch == 1:
    print(1)
else:
    print(0)