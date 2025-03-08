N, M = map(int, input().split())

data = list(map(int, input().split()))
dic = {}
for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

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
        if dic[data[i]] != 0:
            dic[data[i]] -= 1
            result.append(data[i])
            dfs()
            result.pop()
            dic[data[i]] += 1

dfs()