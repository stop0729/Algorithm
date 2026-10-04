def solution(answers):
    array1 = [1,2,3,4,5]
    array2 = [2,1,2,3,2,4,2,5]
    array3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0
    result1 = 0
    result2 = 0
    result3 = 0
    for i in range(len(answers)):
        if answers[i] == array1[count1]:
            result1 += 1
        if answers[i] == array2[count2]:
            result2 += 1
        if answers[i] == array3[count3]:
            result3 += 1
        if count1 == 4:
            count1 = 0
        else:
            count1 += 1
        if count2 == 7:
            count2 = 0
        else:
            count2 += 1
        if count3 == 9:
            count3 = 0
        else:
            count3 += 1
    result = [result1, result2, result3]
    answer = []
    tmp = (max(result))
    for i in range(len(result)):
        if result[i] == tmp:
            answer.append(i+1)
    
    return answer