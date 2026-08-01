def solution(s):
    answer = len(s)
    for step in range(1, (len(s)//2)+1):
        prev = s[0:step]
        count = 1
        final = ''
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                if count >= 2:
                    final = final + str(count) + prev
                else:
                    final = final + prev
                prev = s[j:j+step]
                count = 1
                
        if count >= 2:
            final = final + str(count) + prev
        else:
            final = final + prev
        
        answer = min(answer, len(final))
    
    return answer