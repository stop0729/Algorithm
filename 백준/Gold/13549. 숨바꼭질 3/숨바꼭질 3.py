from collections import deque

N, M = map(int, input().split())

sis = [-1] * (100000+1)
sis[N] = 0

q = deque()
q.append(N)


def bfs():
    
    while q:
        out = q.popleft()

        for i in (out, -1, 1):
            temp = out + i
            if 0<= temp <= 100000 :
                if sis[temp] == -1:
                    if i == out:
                        sis[temp] = sis[out] 
                        q.append(temp)
                    elif i == -1 or i == 1:
                        sis[temp] = sis[out] + 1
                        q.append(temp)



bfs()

print(sis[M])