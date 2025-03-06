N, K = map(int, input().split())

mother = 1
for i in range(N-K+1, N+1):
    mother *= i

child = 1
for i in range(1, K+1):
    child *= i 

print(int(mother / child))