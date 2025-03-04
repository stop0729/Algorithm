import sys
sys.setrecursionlimit(10000)

T = int(input())

def bfs(data, x, y):
    if (x>=0 and x<M) and (y>=0 and y<N):
        if data[y][x] == 1:
            data[y][x] = 0
            bfs(data, x-1, y)
            bfs(data, x, y-1)
            bfs(data, x, y+1)
            bfs(data, x+1, y)
            return 1
    return 0

for i in range(T):
    M, N, K = map(int, input().split())
    data = [[0]*M for i in range(N)]
    result = 0
    for i in range(K):
        X, Y = map(int, input().split())
        data[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1: 
                result += bfs(data, j, i)
            
    print(result)    