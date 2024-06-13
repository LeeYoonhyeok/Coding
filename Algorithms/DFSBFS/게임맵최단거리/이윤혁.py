'''
dfs는 효율성 불통, bfs는 visited를 set으로 하면 효율성 통과
set이 list보다 탐색 속도가 빠르기 때문
'''

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0]) # n : maps 가로길이, m : maps 세로길이
    visited = set([(0, 0)])
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)] # (x, y), 시계방향
    queue = deque([(0, 0, 1)]) # queue
        
    while queue:
        x, y, cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt 
        for i in range(4):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and (nx, ny) not in visited: # 범위, 벽, 방문
                visited.add((nx, ny))
                queue.append((nx, ny, cnt+1))
    return -1
    
            

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
print(solution(maps))



'''
### dfs로 풀었더니 효율성 테스트 불통

def solution(maps):
    global answer
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def dfs(x, y, cnt):
        global answer
        if x == n - 1 and y == m - 1:
            if answer == -1:
                answer = cnt
            else:
                answer = min(answer, cnt)
            return
        
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
        for i in range(4):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = False
    
    visited[0][0] = True
    dfs(0, 0, 1)
    return answer
'''