from collections import deque

N, K = map(int, input().split())

lst = list(map(int, input().split()))

mt = []
answer = 0

# 이 다음으로 오는 2, 3 중 


for i in range(K):
    priority = []
    temp = lst[i]

    if temp in mt:
        continue

    if len(mt) < N:
        mt.append(temp)
        continue
    

    for j in range(len(mt)):
        switch = 0
        for k in range(i+1, K):
            if lst[k] == mt[j]:
                priority.append([mt[j], k])
                switch = 1
                break
        if switch == 0:
            priority.append([mt[j], 101])

    maxx = 0
    for j in range(len(priority)):
        if priority[j][1] > maxx:
            maxx = priority[j][1]
            target = j

    rv = priority[target][0]
    priority.pop(target)
    mt.remove(rv)
    mt.append(temp)
    answer += 1


print(answer)