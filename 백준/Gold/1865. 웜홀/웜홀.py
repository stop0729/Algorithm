tc = int(input())

inf = 10e9

def bellman_ford():
    time = [inf] * (N+1)
    time[1] = 0

    for i in range(N):
        for j in edge:
            cur, next, cost = j
            if time[next] > time[cur] + cost:
                time[next] = time[cur] + cost
                if i == N-1:
                    return True
            
    return False

for i in range(tc):
    N, M, W = map(int, input().split())
    
    edge = []
    for i in range(M):
        a, b, c = map(int, input().split())
        edge.append([a,b,c])
        edge.append([b,a,c])
    
    for i in range(W):
        a, b, c = map(int, input().split())
        edge.append([a,b,-c])

    if bellman_ford():
        print('YES')
    else:
        print("NO")

