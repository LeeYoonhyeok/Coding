# level = n / branch = 4
# 

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_n = -1e9
min_n = 1e9

def dfs(level, total, plus, minus, mul, div): 
    global min_n, max_n
    if level == n: # level 다 되면 종료
        min_n = min(total, min_n)
        max_n = max(total, max_n)
        return
    
    if plus>0:
        dfs(level+1, total + numbers[level], plus-1, minus, mul, div)
    if minus>0:
        dfs(level+1, total - numbers[level], plus, minus-1, mul, div)
    if mul>0:
        dfs(level+1, total * numbers[level], plus, minus, mul-1, div)
    if div>0:
        dfs(level+1, int(total / numbers[level]), plus, minus, mul, div-1)
        
dfs(1,numbers[0], plus, minus, mul, div)
print(max_n)
print(min_n)