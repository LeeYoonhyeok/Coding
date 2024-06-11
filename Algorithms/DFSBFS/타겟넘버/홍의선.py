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
    if len(num_list) == level:
        
        return 0

def solution(numbers, target):
    answer = 0
    num_list = numbers

    return answer