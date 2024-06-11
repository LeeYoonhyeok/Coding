'''
[설계]
dfs depth 최대 20
+ 할지, - 할지 -> branch 2

*시간복잡도
2^20 = 약 100만 => 10ms
'''
num_list = []

def dfs(level, target, sum):
    global num_list
    #  끝날 조건 
    if len(num_list) == level:
        if target == sum:
            return 1
        return 0
    
    # 순회
    plus = sum + num_list[level]
    minus = sum - num_list[level]
    return dfs(level+1, target, plus) + dfs(level+1, target, minus)
    
def solution(numbers, target):
    global num_list
    answer = 0
    num_list = numbers

    answer = dfs(0, target, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))