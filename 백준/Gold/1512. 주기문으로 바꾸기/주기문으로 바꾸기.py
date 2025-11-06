import sys

r = sys.stdin.readline
M = int(r())
s = r().strip()

answer = 9999
while M > 0:
    cnt = 0
    for i in range(M):
        d = {k: 0 for k in "ACGT"}
        for c in s[i::M]:
            d[c] += 1
        v = d.values()
        cnt += sum(v) - max(v)
    answer = min(answer, cnt)
    M -= 1

print(answer)