N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()
isused = [0] * len(lst)
result = []

def back_(count, a):
    if count == M:
        for i in range(M):
            print(result[i], end = ' ')
        print()
        return 
    
    for i in range(len(lst)):
        if isused[i] != 1 and lst[i] > a:
            result.append(lst[i])
            isused[i] = 1
            back_(count+1, lst[i])
            result.pop()
            isused[i] = 0

back_(0, 0)