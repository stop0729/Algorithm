# from collections import deque

# N, K = map(int, input().split())

# data = [-1] * 300000
# q = deque()
# q.append(N)
# data[N] = 0

# while q:
#     if data[K] != -1:
#         print(data[K])
#         break
#         result = data[K]
    
#     now = q.popleft()
#     for i in (now-1, now+1, 2*now):
#         if 0<= i <= 300000:
#             if data[i] == -1:
#                 data[i] = data[now] + 1
#                 q.append(i)

# print(data[:20])

from collections import deque

N, K = map(int, input().split())

data = [-1] * 300000
q = deque()
q.append(N)
data[N] = 0
cnt = 0

while q:
    now = q.popleft()

    if K == now:
        result = data[K]
        cnt += 1 
    
    for i in (now-1, now+1, 2*now):
        if 0<= i < 300000:
            if data[i] == -1 or data[i] == data[now] + 1:
                data[i] = data[now] + 1
                q.append(i)

print(result)
print(cnt)
