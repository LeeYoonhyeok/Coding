def dfs(numbers, target, level, v):
    if len(numbers) == level:
        if v == target:
            global cnt
            cnt += 1
        return

    dfs(numbers, target, level + 1, v + numbers[level])
    dfs(numbers, target, level + 1, v - numbers[level])

def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0) 
    return cnt
