import sys
input = sys.stdin.readline

def transfer(a, b):
    cum = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return cum[a] + b

n = int(input().strip())
segs = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    segs.append((transfer(a, b), transfer(c, d)))

START = transfer(3, 1)
TARGET = transfer(12, 1)  # 11/30까지 덮이려면 12/1에 도달
# 시작 오름차순, 시작 같으면 끝 내림차순
segs.sort(key=lambda x: (x[0], x[1]))

cur = START
ans = 0
i = 0
best = cur

while cur < TARGET:
    updated = False
    while i < n and segs[i][0] <= cur:
        if segs[i][1] > best:
            best = segs[i][1]
            updated = True
        i += 1
    if not updated:
        print(0)
        break
    ans += 1
    cur = best
else:
    print(ans)