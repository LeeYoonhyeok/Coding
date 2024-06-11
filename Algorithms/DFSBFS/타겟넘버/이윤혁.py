def solution(numbers, target):
    
    def dfs(level, sum):
        if level == len(numbers):
            if sum == target:
                return 1
            return 0

        return dfs(level+1, sum+numbers[level]) + dfs(level+1, sum-numbers[level])
    
    return dfs(0, 0)
