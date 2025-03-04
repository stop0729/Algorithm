com = int(input())
con = int(input())

data = [[] for i in range(com+1)]
for i in range(con):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

result = [0] * (com+1)
start = 1
result[start] = 1
s = []
s.append(start)

while s:
    out = s.pop()
    for i in data[out]:
        if result[i] != 1:
            s.append(i)
            result[i] = 1

total = 0
for i in range(len(result)):
    if result[i] == 1:
        total += 1

print(total-1)