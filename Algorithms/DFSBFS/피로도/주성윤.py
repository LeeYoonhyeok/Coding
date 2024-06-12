# level : max는 8까지 / branch : 던전 선택도 8개까지
# 모든 던전을 다 돌면서 체크 --> dfs
# 던전을 돌기전에 k >= 던전[][0] 체크
# k는 던전[][1]을 계속 빼간다
# 중복 방지를 위해 visited 배열을 사용
# dfs와 solution 기능별 구분

def dfs(k, dungeons, visited, cnt):
    global answer # 전역변수 지정
    answer = max(answer, cnt) 
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]: # 두 조건 만족시, 만족 못하면 재귀 호출 종료
            visited[i] = True # 방문 기록
            dfs(k-dungeons[i][1], dungeons, visited, cnt+1) 
            visited[i] = False # 조건 충족이 안된 던전에서 빠져나와 방문 초기화(백트래킹)

def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False]*len(dungeons)
    dungeons.sort(key = lambda x : x[0], reverse=True) # 최소피로도 오름차 정렬
    dfs(k, dungeons, visited, 0) # cnt 0부터 출발
    return answer
