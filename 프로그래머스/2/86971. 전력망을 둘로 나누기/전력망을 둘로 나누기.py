# 리스트 안에 값이 두개로 나눠져 있을때 이것들의 개수 비교하는 방법

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

def find_diff(i, n, wires):
    parent = [i for i in range(n+1)]
    wires.sort()
    
    for j in wires:
        if i == j:
            continue
        a, b = j
        union_parent(parent, a, b)
    
    num_a = 1
    num_b = 0
    
    temp = parent[1]

    for j in range(2, len(parent)):
        if find_parent(parent, j) == temp:
            num_a += 1
        else:
            num_b += 1
    return abs(num_a - num_b)
    

def solution(n, wires):
    answer = 1e9
    for i in wires:
        temp = find_diff(i, n, wires)
        answer = min(answer, temp)
        
    return answer