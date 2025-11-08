N = int(input())

lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
    
lst.sort(key = lambda x : x[1], reverse=True)
prior = lst[0][1] - lst[0][0]

for i in range(1, N):
    t, end = lst[i]
    if prior <= end:
        prior -= t
    else:
        prior = end - t

if prior < 0:
    prior = -1
    
print(prior)