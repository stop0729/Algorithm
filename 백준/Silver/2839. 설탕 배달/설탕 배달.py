N = int(input())

a = N // 5
result = 1e9
switch = -1

for j in range(a+1):
    if (N - j*5) % 3 == 0:
        temp = (N - j*5) // 3
        switch = 0 
        if temp + j < result:
            result = temp + j
            
if switch == -1:
    print(-1)
else:
    print(result)