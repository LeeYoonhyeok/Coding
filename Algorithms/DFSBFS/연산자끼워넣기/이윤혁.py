import sys
input = sys.stdin.readline

n = 6
num = [1, 2, 3, 4, 5, 6]
op = [2, 1, 1, 1] # +, -, *, /
result = []

def dfs(level, temp):
    if level == n-1:
        result.append(temp)
        return
    if op[0] > 0:
        op[0] -= 1
        dfs(level+1, temp + num[level+1])
        op[0] += 1
        
    if op[1] > 0:
        op[1] -= 1
        dfs(level+1, temp - num[level+1])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(level+1, temp * num[level+1])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if temp < 0:
            temp *= -1
            temp //= num[level+1]
            temp *= -1
        else:
            temp //= num[level+1]
        dfs(level+1, temp)
        op[3] += 1

dfs(0, num[0])
print(max(result))
print(min(result))