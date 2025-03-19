import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a > b:
        parent[a] = b

    else:
        parent[b] = a

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    elif a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print('YES')
        else:
            print('NO')