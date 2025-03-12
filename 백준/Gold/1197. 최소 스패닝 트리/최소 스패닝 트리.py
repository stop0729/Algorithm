def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

edges = []
for i in range(E):
    start, end, cost = map(int, input().split())
    edges.append((cost, start, end))

edges.sort()

result = 0
for i in edges:
    cost, start, end = i
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        result += cost

print(result)