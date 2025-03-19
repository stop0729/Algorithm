N, M = map(int, input().split())
serial = [0] * M
isused = [0] * N


def func(k):
    if (k==M):
        for i in range(M):
            print(serial[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if(isused[i-1] == 0):
            serial[k] = i
            isused[i-1] = 1
            func(k+1)
            isused[i-1] = 0

func(0)
