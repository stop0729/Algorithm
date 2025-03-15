N, M = map(int, input().split())

data1 = [list(map(int, input().split())) for i in range(N)]

M, K = map(int, input().split())

data2 = [list(map(int, input().split())) for i in range(M)]

data3 = []

for i in range(N):
    lst = []
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += data1[i][k] * data2[k][j]
        lst.append(temp)
    data3.append(lst)

for i in range(N):
    for j in range(K):
        print(data3[i][j], end = ' ')
    print()