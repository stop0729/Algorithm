import sys
sys.setrecursionlimit(10**5)

def dfs(start, l, word, lst, string):
    if start == l:
        lst.append(string)
        return
    
    for i in range(0, len(word)):
        string += word[i]
        dfs(start+1, l, word, lst, string)
        string = string[:-1]

def solution(word):
    answer = 0
    result = []

    for i in range(1, 6):
        lst = []
        string = ""
        dfs(0, i, "AEIOU", lst, string)
        result = result + lst
    
    result.sort()
    answer = result.index(word)+1

    return answer