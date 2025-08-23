answer = 0 

def dfs(cnt, target, result, numbers):
    global answer
    if cnt == len(numbers):
        if result == target:
            answer += 1
        return

    dfs(cnt+1, target, result + numbers[cnt], numbers)
    dfs(cnt+1, target, result - numbers[cnt], numbers)
    

def solution(numbers, target):

    dfs(0, target, 0, numbers)
    
    return answer