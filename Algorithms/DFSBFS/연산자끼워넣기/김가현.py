import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

max_n = -1e9
min_n = 1e9

def dfs(level, total, plus, minus, mult, div):
    global max_n, min_n
    if level == n:
        max_n = max(total, max_n)
        min_n = min(total, min_n)
        return
    
    if plus:
        dfs(level + 1, total + num[level], plus - 1, minus, mult, div)
    if minus:
        dfs(level + 1, total - num[level], plus, minus - 1, mult, div)
    if mult:
        dfs(level + 1, total * num[level], plus, minus, mult - 1, div)
    if div:
        if total < 0:
            dfs(level + 1, -(-total // num[level]), plus, minus, mult, div - 1)
        else:
            dfs(level + 1, total // num[level], plus, minus, mult, div - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_n)
print(min_n)
