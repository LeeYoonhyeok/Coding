'''
DFS에 대한 강의 수강.
차근차근 들으며 스택 개념이 들어있는 것까지 알고 나니 확실히 이해도가 올라간 듯.
강의에서 설명된 예제와 다른 분들 코드 참조하며 작성.
'''

'''
levels 8
branchs 8
8^8 = 17m

duns[던전번호][0=최소필요피로, 1=소모피로]
'''


def dfs(duns, k, visited, cnt):
    max_cnt = cnt
    
    for i in range(len(duns)):
        if not visited[i] and k >= duns[i][0]:
            visited[i] = True
            max_cnt = max(max_cnt, dfs(duns, k - duns[i][1], visited, cnt + 1))
            visited[i] = False
    
    return max_cnt
        
    
    
def solution(k, duns):
    visited = [False] * len(duns)
    
    return dfs(duns, k, visited, 0)