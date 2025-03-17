import sys

input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

start, end = 0, 0
temp = data[0]
result = 1e9

while True:

    if temp >= S:
        if end - start< result:
            result = end - start
        temp -= data[start]
        if start == end:
            start += 1
            end += 1
        else:
            start += 1

    else:
        end += 1
        if end > len(data)-1:
            break
        temp += data[end]

if result == 1e9:
    print(0)
else:
    print(result + 1)