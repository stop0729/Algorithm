import sys

input = sys.stdin.readline
N, M = map(int, input().split())

data = list(map(int, input().split()))
long = max(data)

start = 0 
end = long
result = 0

while end >= start:
    com = (start + end) // 2
    temp = 0
    for i in range(len(data)):
        diff = data[i] - com
        if diff < 0 :
            diff = 0
        temp += diff
    if temp < M :
        end = com - 1
    elif temp >= M:
        start = com + 1
        if com > result:
            result = com

print(result)