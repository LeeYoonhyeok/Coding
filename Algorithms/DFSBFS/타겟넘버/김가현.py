def dfs(numbers, target, level, sum):
    
    global cnt
    n = len(numbers)
    cnt = 0
    
    if n == level & sum == target:
        cnt += 1
        return
    
    elif n == level:
        return
    
    dfs(numbers, target, level + 1, sum + numbers[level])
    dfs(numbers, target, level + 1, sum - numbers[level] )
    
    return 

def solution(numbers, target):
    
    global cnt 
    
    dfs(numbers, target, 0,0)
    
    return cnt