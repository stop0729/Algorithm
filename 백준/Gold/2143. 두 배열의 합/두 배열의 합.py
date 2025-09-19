import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

ans = 0
dictA = defaultdict(int)

for i in range(n):
    for j in range(i+1, n+1):
        dictA[sum(A[i:j])] += 1

ans = 0
for i in range(m):
    for j in range(i+1, m+1):
        ans += dictA[T - sum(B[i:j])]

print(ans)