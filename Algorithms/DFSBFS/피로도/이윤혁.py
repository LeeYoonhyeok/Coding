'''
dungeons 구조 : [["최소 필요 피로도", "소모 피로도"]]
"최소 필요 피로도"는 >= "소모 피로도"
탐험 가능한 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

시간 내 못 풂.. 가현님꺼 참고함. 내일 다시 풀어보기 (2024-06-12)
'''
def solution(k, dungeons):
    global answer
    answer = -1
    visted = [False] * len(dungeons)
    dfs(k, visted, dungeons, 0)
    return answer

def dfs(k, visited, dungeons, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], visited, dungeons, cnt+1)
            visited[i] = False

dungeons = [[80,20],[50,40],[30,10]]	
k = 80
print(solution(k, dungeons))