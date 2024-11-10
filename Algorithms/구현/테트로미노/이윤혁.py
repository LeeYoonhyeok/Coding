'''
한 포인트에서 4번 움직이는 모든 경우의 수가 테트로미노 전체 경우의 수랑 같음
(한 포인트에서 4번 아무렇게나 움직여보면 테트로미노 모양과 전체가 일치)
-> 한 포인트에서 겹치지 않게 4번 움직여서 모든 경우의 수의 최대합 전역변수 최대합 비교
-> 'ㅗ'모양은 4번 움직여서 나오는 모양이 아니기에 따로 탐색

# 'ㅗ'모양 탐색 방법
    '
'   "   '
    '
" 포인트에서 상하좌우 모두 탐방하여 리스트에 넣은 후 최솟값 제거하면 'ㅗ'모양의 최대합 완성
그 후 " 포인트의 최대합과 전역변수 최대합 비교
'''
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [(-1,0), (1,0), (0,-1), (0,1)] #상하좌우
maximum = 0

# ㅗ 모양을 제외한 나머지 모양 탐색
def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4: # 4번째면 종료
        maximum = max(maximum, tmp)
        return
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:                
            visited[nx][ny] = True
            dfs(nx, ny, tmp+graph[nx][ny], cnt+1)
            visited[nx][ny] = False

# ㅗ 모양 탐색
def check_other_shape(x, y):
    global maximum
    tmp = graph[x][y]
    arr = []
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:       
            arr.append(graph[nx][ny])
    length = len(arr)
    if length == 4 : # 4개 모두 들어갔으면 최소값 하나 빼서 'ㅗ'모양 만든 후 sum
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + tmp)
    elif length == 3: # 3개 들어갔으면 'ㅗ'모양이므로 바로 sum
        maximum = max(maximum, sum(arr) + tmp)
    return # 2개 들어갔으면 'ㅗ'모양이 아니므로 return

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        check_other_shape(i, j)
        visited[i][j] = False

print(maximum)