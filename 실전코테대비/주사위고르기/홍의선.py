'''
주사위 최대 10개

주사위 고르는 경우의 수 * A 주사위의 숫자 경우의 수 * B 주사위 숫자 경우의 수
10C5 * 6^5 * 6^5
250 * 8000 * 8000 = 너무 크다

주사위 조합별로 미리 숫자 구성을 구한다면?
10C5 * 6^5 = 2000만

그다음, A의 조합과 B의 조합의 합들을 정렬하여 
A의 조합의 각 값보다 작은 B 조합 합들의 개수와 큰 B 조합 합들의 개수를 구한다.
이때 가장 승리가 많은 조합을 저장한다.
정렬 : (8000 + 8000) * log16000
탐색 : 16000

'''
hash_table = dict()
def create_hashkey(selected):
    hash_key = 0
    for num in selected:
        hash_key += num 
        hash_key *= 10
        
    return hash_key

def cal(level, sum, dice, selected, hashkey):
    global hash_table
    
    if level == len(selected):
        if not hashkey in hash_table:
            hash_table[hashkey] = [0]*501
        hash_table[hashkey][sum] += 1
        return 
    
    d_num = selected[level]
    for i in range(6):
        sum += dice[d_num][i]
        cal(level + 1, sum, dice, selected)
        sum -= dice[d_num][i]
        
        
        
def dfs(level, dice, selected, visited):  # 2000만
    dice_cnt = len(dice)
    if level == (dice_cnt/2):
        hashkey = create_hashkey(selected)
        cal(0, 0, dice, selected, hashkey)
        return
    
    for i in range(dice_cnt):
        if visited[i]:
            continue
        
        selected.append(i)
        visited[i] = True 
        
        dfs(level + 1, dice, selected, visited)
        
        selected.pop()
        visited[i] = False
        

def solution(dice):
    global hash_table
    answer = []
    dice_cnt = len(dice)
    
    dfs(0, dice, [], [False] * 10)  # hash_table 완성
    
    # 다시한번 dfs 10C5 로 주사위 선택해서 나머지 주사위 조합들하고 크기 비교
    # 250 * 25만
    
    return answer