N, M = map(int, input().split())

data = list(map(int, input().split()))
data.sort()


result = []

def dfs():

    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(0, N):
        if data[i] not in result:
            result.append(data[i])
            dfs()
            result.pop()

dfs()