

def solution(number, k):
    lst = []
    for i in number:
        lst.append(int(i))
    
    stack = []
    
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k = k - 1
        stack.append(i)
    
    answer = ''.join(stack[:len(stack)-k])
        
    return answer