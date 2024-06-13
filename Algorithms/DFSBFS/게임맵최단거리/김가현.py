# 0 -> 벽, 1 -> 길
from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1 # 방문

    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                
                # 방문한 적이 없는 좌표이고 지도에 길이 존재해야함
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
    return visited[n-1][m-1] if visited[n-1][m-1] > 0 else -1