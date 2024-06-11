def solution(numbers, target):
    ans = 0
    def dfs(level, sum):
        global ans
        if level == len(numbers):
            if sum == target:
                return 1
            return 0

        return dfs(level+1, sum+numbers[level]) + dfs(level+1, sum-numbers[level])
    
    return dfs(0, 0)