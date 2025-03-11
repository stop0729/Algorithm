import sys
sys.setrecursionlimit(10**5)

v = int(input())

graph = [[] for i in range(v+1)]

for i in range(v):
    temp = list(map(int, input().split()))
    
    result = 0
    for i in range(1, len(temp)):
        if temp[i] != -1:
            if result % 2 == 0:
                graph[temp[0]].append([])
                graph[temp[0]][result//2].append(temp[i])
                result += 1
            else:
                graph[temp[0]][result//2].append(temp[i])
                result += 1
                
def dfs(node):
    for i in graph[node]:
        new_node, dist = i
        if distance[new_node] == -1:
            distance[new_node] = dist + distance[node]
            dfs(new_node)

distance = [-1] * (v+1)
distance[1] = 0
dfs(1)
temp = max(distance)
new_node = distance.index(temp)

distance = [-1] * (v+1)
distance[new_node] = 0
dfs(new_node)
print(max(distance))