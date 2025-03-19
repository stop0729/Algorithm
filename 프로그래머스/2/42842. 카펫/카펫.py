import math

def division(num):
    data = []
    
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            data.append([num//i, i])
    return data


def solution(brown, yellow):
    
    comb = division(brown+yellow)

    for i in comb:
        x, y = i
        if (x-2)*(y-2) == yellow:
            return [x, y]