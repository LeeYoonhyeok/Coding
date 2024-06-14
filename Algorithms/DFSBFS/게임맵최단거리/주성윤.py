# bfs 알고리즘 다시 복습 후 유효성 확인 함수를 따로 나눠서 작성
# visited는 방문용으로만 쓰고 cnt로 확인

from collections import deque

def is_valid_move(n, m, dx, dy, maps): #유효한지 확인
    return 0 <= dx < n and 0 <= dy < m and maps[dx][dy]
    
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dir = [(0,1), (-1,0), (0, -1), (1,0)]
    queue = deque([(0,0,1)]) # x, y, 시작칸
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == n-1 and y == m-1: # 종료 조건
            return cnt
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            if is_valid_move(n,m,dx,dy,maps) and not visited[dx][dy]:
                queue.append((dx,dy,cnt+1))
                visited[dx][dy] = True
    return -1
