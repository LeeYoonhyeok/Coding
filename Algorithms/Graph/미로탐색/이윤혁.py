import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, maze):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    queue = deque([(0,0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return maze[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                
                
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(N, M, maze))