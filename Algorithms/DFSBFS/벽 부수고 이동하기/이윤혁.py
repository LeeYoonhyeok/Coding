'''
** 다시 풀어보기 **
최단거리 -> bfs
벽 : 1 / 빈 곳 : 0
벽 부술 수 있음.. -> visited 3차원으로 구성해서 마지막 벽 부쉈는지 체크
벽을 부쉈으면 1
벽을 부순 횟수가 (이전 횟수 + 1)회보다 크다면 벽을 부수고 (이전 횟수 + 1)로 visited에 기록..
'''

import sys
from collections import deque

def bfs(N, M, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
       
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, break_wall)
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    
    while queue:
        x, y, break_wall = queue.popleft()
        
        # 목적지 도달
        if x == N-1 and y == M-1:
            return min(visited[x][y][0], visited[x][y][1])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 공간
                if grid[nx][ny] == '0':
                    if visited[nx][ny][break_wall] > visited[x][y][break_wall] + 1:
                        visited[nx][ny][break_wall] = visited[x][y][break_wall] + 1
                        queue.append((nx, ny, break_wall))
                # 벽
                elif grid[nx][ny] == '1' and break_wall == 0:
                    if visited[nx][ny][1] > visited[x][y][0] + 1:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx, ny, 1))
    
    # 도착점에 도달하지 못한 경우
    return -1

N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(sys.stdin.readline().strip())

result = bfs(N, M, grid)
print(result)
