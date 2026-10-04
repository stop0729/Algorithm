def solution(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)  # 열린 괄호는 스택에 저축
        else:  # char == ")" 인 경우
            if not stack:  # 꺼낼 열린 괄호가 없다면 실패
                return False
            stack.pop()  # 짝이 맞으므로 스택에서 하나 제거
            
    # 문자열을 다 돌았을 때 스택이 완전히 비어있어야 True
    return len(stack) == 0