q = [-1]

n = int(input())
check = 1
result = []
p = 0
m = 0

for i in range(n):
    num = int(input())
    while True:
        if q[-1] == num:
            last = q.pop(-1)
            result.append('-')
            m += 1
            break
        elif check == n+1:
            break
        else:
            q.append(check)
            result.append('+')
            p += 1
            check += 1

if p == m:
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')