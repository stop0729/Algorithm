N, M = map(int, input().split())

data = list(map(int, input().split()))

data.sort()


result = []
s = set()

def dfs():

    if len(result) == M:
        temp = ' '.join(map(str, result))
        if temp not in s:
            print(temp)
            s.add((temp))
        return

    for i in range(0, N):
        if len(result) != 0:
            if data[i] < max(result):
                continue
        result.append(data[i])
        dfs()
        result.pop()

dfs()