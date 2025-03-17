import math

N = int(input())

odd = []

for i in range(2,N+1):
    temp = int(math.sqrt(i))+1
    flag = False
    for j in range(2, temp):
        if i % j == 0:
            flag = True
            break
    if flag == False:
        odd.append(i)


def two_pointer(N):
    if len(odd) == 0:
        print(0)
        return
    else:
        sum = odd[0]
    
    start, end = 0, 0
    result = 0
    while True:
        if sum <= N:
            if sum == N:
                result += 1
            end += 1
            if end >= len(odd):
                break
            sum += odd[end]
        else:
            if start == end:
                end += 1
                if end >= len(odd):
                    break
                sum += odd[end]
            sum -= odd[start]
            start += 1

    print(result)

two_pointer(N)
