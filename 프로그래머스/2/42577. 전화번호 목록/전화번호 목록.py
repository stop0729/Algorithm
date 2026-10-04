def solution(phone_book):
    
    phone_dict = {}
    for i in phone_book:
        if i not in phone_dict:
            phone_dict[i] = 1
        else:
            phone_dict[i] += 1
    
    for i in phone_book:
        if phone_dict[i] >= 2:
            return False
        tmp = ""
        for j in range(len(i)-1):
            tmp += i[j]    
            if tmp in phone_dict:
                return False
    return True