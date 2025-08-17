def dfs(idx, cnt):
    if cnt == m:
        print(' '.join(map(str, serial)))
        return
    
    for i in range(idx, n):
        serial[cnt] = lst[i]
        dfs(i+1, cnt+1)

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    else:
        n = len(temp)-1
        m = 6
    lst = temp[1:]

    serial = [0] * m
    dfs(0, 0)
    print()