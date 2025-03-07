from collections import deque

N, K = map(int, input().split())

if K < N:
    big = N
else:
    big = K

data = [-1] * (2 * big + 1)
data[N] = 0
q = deque()
q.append(N)

def bfs(data):
    while q:
        out = q.popleft()
        for i in [-1, 1, out]:
            n_out = out + i
            if 0<= n_out < 2 * big and data[n_out] == -1:
                data[n_out] = data[out] + 1
                q.append(n_out)
                
bfs(data)

print(data[K])