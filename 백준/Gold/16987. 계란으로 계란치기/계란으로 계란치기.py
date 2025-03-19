N = int(input())

data = []
for i in range(N):
    s, w = map(int, input().split())
    data.append([s, w])

def check(data):
    temp = 0
    for i in range(len(data)):
        if data[i][0] <= 0:
            temp+=1
    return temp

def brute(start):
    global result

    if start == N:
        result = max(result, check(data))
        return

    if data[start][0] <= 0:
        brute(start+1)
    
    else:
        all_broken = True
        for i in range(len(data)):
            if data[i][0] > 0 and i != start:
                all_broken = False
                data[i][0] -= data[start][1]
                data[start][0] -= data[i][1]
                brute(start + 1)
                data[i][0] += data[start][1]
                data[start][0] += data[i][1]
        if all_broken:
            brute(N)

result = 0
brute(0)

print(result)