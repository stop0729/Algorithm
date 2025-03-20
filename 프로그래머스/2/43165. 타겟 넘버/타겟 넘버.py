from itertools import combinations

def solution(numbers, target):
    temp = [i for i in range(len(numbers))]
    total = sum(numbers)
    answers = 0
    
    for i in range(1, len(numbers)+1):
        result = list(combinations(temp, i))
        for j in result:
            temp2 = 0
            for k in j:
                temp2 += numbers[k]
            if total - temp2*2 == target:
                answers += 1

    return answers