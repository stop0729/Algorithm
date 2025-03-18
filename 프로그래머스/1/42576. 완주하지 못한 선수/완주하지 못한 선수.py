from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)

    sum_hash = 0

    for i in participant:
        dic[hash(i)] = i
        sum_hash += hash(i)

    for i in completion:
        sum_hash -= hash(i)
    answer = dic[sum_hash]

    return answer