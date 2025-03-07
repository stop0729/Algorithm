import sys

input = sys.stdin.readline
N, M = map(int, input().split())

set_N = set()
set_M = set()


for i in range(N):
    set_N.add(input().strip())
for j in range(M):
    set_M.add(input().strip())


result = list(set_N & set_M)
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])