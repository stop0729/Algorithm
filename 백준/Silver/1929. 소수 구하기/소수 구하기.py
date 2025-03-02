import math

a, b = map(int, input().split())
if a == 1:
    a = 2

for i in range(a, b+1):
    switch = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            switch = -1
            break
    if switch == 0:
        print(i)