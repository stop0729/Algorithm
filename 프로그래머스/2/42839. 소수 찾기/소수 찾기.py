import math
from itertools import permutations

def odd(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def make_num(string):
    result = set()
    for i in range(1, len(string)+1):
        b = permutations(string, i)
        for j in b:
            j = list(j)
            j = ''.join(map(str, j))
            if j[0] != '0' and j != "1":
                j = int(j)
                result.add(j)
    return result

# 문자열이 주어졌을때 그것들의 조합으로 숫자를 만들어보자.
def solution(numbers):
    
    result = make_num(numbers)
    print(result)
    answer = 0
    
    for i in result:
        if odd(i) == True:
            answer += 1
    
    return answer