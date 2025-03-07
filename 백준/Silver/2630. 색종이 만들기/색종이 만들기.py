N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

result = [0, 0]

def dfs(a, b, n):
    temp = data[a][b]
    for i in range(n):
        for j in range(n):
            if data[a+i][b+j] != temp:
                dfs(a, b, n//2)
                dfs(a + n//2, b, n//2)
                dfs(a, b + n//2, n//2)
                dfs(a + n//2, b + n//2, n//2)
                return 0
    if temp == 0:
        result[0] = result[0] + 1
    elif temp == 1:
        result[1] = result[1] + 1

dfs(0, 0, N)

print(result[0])
print(result[1])