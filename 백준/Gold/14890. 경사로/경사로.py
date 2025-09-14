n, l = map(int, input().split())

graph = []

def det_same(lst):
    temp = lst[0] 
    for i in range(1, len(lst)):
        if lst[i] != temp:
            return False
    
    return True

result1 = 0
result2 = 0

for i in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)


for i in range(n):
    switch1 = 0
    if det_same(graph[i]) == True:
        result1 += 1
    else:
        step1 = -1 # 겹치는지 판단
        for j in range(0, n-1):
            if graph[i][j] != graph[i][j+1]:
                if abs(graph[i][j] - graph[i][j+1]) != 1:
                    switch1 = 1
                    break
                if graph[i][j] > graph[i][j+1]:
                    if (j+l <n) and det_same(graph[i][j+1:j+l+1]) == True:
                        step1 = j+l
                        pass
                    else:
                        switch1 = 1
                        break
                else:
                    if step1 >= j-l+1: # 발판을 새로 놓을 위치에 이전 발판이 안겹치면
                        switch1 = 1
                        break
                    if (j-l+1 >=0) and det_same(graph[i][j-l+1:j+1]) == True:
                        step1 = j
                        pass
                    else:
                        switch1 = 1
                        break

        if switch1 == 0:
            result1 += 1

    switch2 = 0
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    
    if det_same(temp) == True:
        result2 += 1
    else:
        step2 = -1
        for j in range(0, n-1):
            if temp[j] != temp[j+1]:
                if abs(temp[j] - temp[j+1]) != 1:
                    switch2 = 1
                    break
                if temp[j] > temp[j+1]:
                    if (j+l <n) and det_same(temp[j+1:j+l+1]) == True:
                        step2 = j+l
                        pass
                    else:
                        switch2 = 1
                        break
                else:
                    if step2 >= j-l+1: # 발판을 새로 놓을 위치에 이전 발판이 안겹치면
                        switch2 = 1
                        break
                    if j-l+1 >=0 and det_same(temp[j-l+1:j+1]) == True:
                        step2 = j
                        pass
                    else:
                        switch2 = 1
                        break

        if switch2 == 0:
            result2 += 1

print(result1+result2)