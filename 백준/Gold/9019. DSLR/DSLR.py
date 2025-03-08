from collections import deque

T = int(input())



for i in range(T):

    visited = [False for i in range(10001)]
    a, b = map(int, input().split())
    
    q = deque()
    q.append([a, ''])
    while q:
        num, command = q.popleft()

        if num == b:
            print(command)
            break
        
        D = (num*2) % 10000
        if visited[D] != True:
            visited[D] = True
            q.append([D, command + 'D'])
        
        S = num-1 if num >= 1 else 9999
        if visited[S] != True:
            visited[S] = True
            q.append([S, command + 'S'])

        L = num // 1000 + (num % 1000) * 10
        if visited[L] != True:
            visited[L] = True
            q.append([L, command + 'L'])

        R = num // 10 + (num % 10) * 1000
        if visited[R] != True:
            visited[R] = True
            q.append([R, command + 'R'])