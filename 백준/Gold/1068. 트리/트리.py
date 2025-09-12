N = int(input())

node = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for i in range(N):
    if node[i] != -1:
        graph[node[i]].append(i)
    else:
        start = i

erase = int(input())

result = 0

def dfs(S, parent):
    global result
    if S == erase and len(graph[parent]) == 1:
        result += 1
        return
    
    elif S == erase:
        return
    
    elif len(graph[S]) == 0:
        result += 1 
        return
    
    for i in graph[S]:
        dfs(i, S)

dfs(start, -1)
if erase == start:
    print(0)
else:
    print(result)