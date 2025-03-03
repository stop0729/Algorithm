K, N = map(int, input().split())

temp = []
for i in range(K):
    temp.append(int(input()))

m = max(temp)
start = 1
end = m
middle = m
result = -1

while start <= end:
    switch = 0

    for i in range(len(temp)):
        switch += temp[i] // middle

    if switch >= N:
        if middle > result:
            result = middle
        start = middle + 1
        middle = int((start + end) / 2)

    else:
        end = middle - 1
        middle = int((start + end) / 2)

print(result)
        