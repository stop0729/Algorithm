N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = 0

result = 0
while end <= len(data)-1:
    temp = sum(data[start:end+1])
    if temp == M:
        result += 1
        end += 1
    elif temp > M:
        if start == end:
            start += 1
            end += 1
        else:
            start += 1
    elif temp < M:
        end += 1
        
print(result)