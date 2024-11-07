import sys
from collections import deque

def solution(arr, operations):
    reverse_flag = False
    
    for op in operations:
        if op == 'R': # 뒤집기
            reverse_flag = not reverse_flag
            
        elif op == 'D': # 버리기
            if len(arr) == 0:
                return 'error'        
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()
                
    if reverse_flag:
        arr.reverse()
    
    return "[" + ",".join(map(str, arr)) + "]" if arr else "[]"

tc = int(sys.stdin.readline())
for _ in range(tc):
    operations = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    string_arr = sys.stdin.readline().strip()
    if n == 0:
        if 'D' in operations:
            print('error')
            continue
        arr = deque()
    else:
        arr = deque(map(int, string_arr[1:-1].split(',')))
    print(solution(arr, operations))