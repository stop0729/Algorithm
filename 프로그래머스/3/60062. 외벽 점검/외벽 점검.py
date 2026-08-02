from itertools import permutations

def solution(n, weak, dist):
    l = len(weak)

    for i in range(l):
        weak.append(weak[i] + n)
    answer = int(1e9)
    
    for i in range(0, l):
        for friends in permutations(dist, len(dist)):
            count = 1
            position = weak[i] + friends[count-1]
            for j in range(i, i+ l):
                if position >= weak[j]:
                    continue
                else:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[j] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer