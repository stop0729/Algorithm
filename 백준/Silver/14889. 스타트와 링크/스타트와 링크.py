N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

result = 1e9
set1 = set()
whole = set([i for i in range(1, N+1)])

def brute(start):
    global result
    if len(set1) == N//2:
        temp1 = 0
        temp2 = 0
        set2 = whole - set1
        s1 = list(set1)
        s2 = list(set2)
        if min(s1) == N//2:
            return

        for i in range(len(s1)):
            for j in range(i+1, len(s1)):
                temp1 += data[s1[i]-1][s1[j]-1] + data[s1[j]-1][s1[i]-1]
                temp2 += data[s2[i]-1][s2[j]-1] + data[s2[j]-1][s2[i]-1]

        if abs(temp1-temp2) < result:
            result = abs(temp1 - temp2)

    for i in range(start, N+1):
        set1.add(i)
        brute(i+1)
        set1.remove(i)           

brute(1)
print(result)