N, M = map(int, input().split())
serial = [0] * M
isused = [0] * N


def func(k, rise):
    if (k==M):
        for i in range(M):
            print(serial[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if(isused[i-1] == 0 and i>rise):
            rise = i
            serial[k] = i
            isused[i-1] = 1
            func(k+1, rise)
            isused[i-1] = 0

func(0, 0)
