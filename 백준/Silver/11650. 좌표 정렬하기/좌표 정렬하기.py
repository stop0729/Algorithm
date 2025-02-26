n = int(input())
store = []

for i in range(n):
    a, b = map(int ,input().split())
    store.append([a,b])
    
store.sort()

for i in store:
    print(i[0], i[1])