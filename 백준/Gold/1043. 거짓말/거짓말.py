N, M = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y, know_truth):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a in know_truth and b in know_truth:
        return
    
    if a in know_truth and b not in know_truth:
        parent[b] = a
    
    elif b in know_truth and a not in know_truth:
        parent[a] = b

    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

parent = []
for i in range(N+1):
    parent.append(i)

people = list(map(int, input().split()))
know_truth = people[1:]

party = [list(map(int, input().split())) for i in range(M)]


for i in range(M):
    if len(party[i]) == 2:
        continue
    else:
        party_len = party[i][0]
        party_people = party[i][1:]
        
        for j in range(party_len-1):
            union_parent(parent, party_people[j], party_people[j+1], know_truth)

result = M
for i in range(M):
    for j in range(1, party[i][0]+1):
        if find_parent(parent, party[i][j]) in know_truth:
            result -= 1
            break

print(result)