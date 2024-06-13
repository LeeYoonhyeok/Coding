'''
최소 피로도 : 탐험 전 필요
소모 피로도 : 탐험 후 소모
dungeons = [최소 피로도, 소모 피로도]
k = 현재 유저 피로도

탐험 할 수 있는 최대 던전 수 

'''  
def dfs(k, dungeons, visited, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k- dungeons[i][1], dungeons, visited, cnt + 1)
            visited[i] = False

def solution(k, dungeons):
    global answer
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    dfs(k, dungeons, visited, 0)
    return answer