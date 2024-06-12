'''
던전 개수 8개 -> level
던전 선택 8개 -> branch

*시간복잡도
8^8 = 2^24 = 1600만


'''
max_cnt = 0

def explore(level, fatigue, cnt, dungeons, visited):  # 깊이, 현재 피로도, 탐험한 던전 개수, 던전 list
    global max_cnt
    
    # 끝날 조건
    if level == len(dungeons):
        # 비교
        if cnt > max_cnt:
            max_cnt = cnt
        return
      
    # 던전 탐험 순서 조합
    for i in range(len(dungeons)):
        if visited[i]: 
            continue 
        
        visited[i] = True
        
        if fatigue < dungeons[i][0]:
            explore(level + 1, fatigue, cnt, dungeons, visited)
        else:
            explore(level + 1, fatigue - dungeons[i][1], cnt + 1, dungeons, visited)
            
        visited[i] = False 
               
    
def solution(k, dungeons):
    global max_cnt
    visited = [False] * len(dungeons)
    explore(0, k, 0, dungeons, visited)
    answer = max_cnt
    
    return answer

# TEST 용 코드
k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))