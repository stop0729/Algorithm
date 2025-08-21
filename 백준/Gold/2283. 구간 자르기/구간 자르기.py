N, K = map(int, input().split())

maxx = 1000000

diff = [0] * (maxx+1)
for _ in range(N):
    a, b = map(int, input().split())
    diff[a] += 1
    diff[b] -= 1

cnt = [0] * (maxx+1)
cur = 0

for i in range(maxx+1):
    cur += diff[i]
    cnt[i] = cur

A = B = 0
acc = 0
flag = False

while A<= maxx and B<= maxx:
    if acc<K:
        acc += cnt[B]
        B += 1
    elif acc>K:
        acc -= cnt[A]
        A += 1
    else:
        flag = True
        break

if flag == True:
    print(A, B)
else:
    print(0, 0)