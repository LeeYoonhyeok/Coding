'''
dfs로 시도했다가 실패. "최단거리 찾을 땐 bfs !!"를 몸소 체험.
bfs도 처음 배웠지만 dfs 덕분에 비교적 쉽게 학습.
n x m 행렬 구성을 거꾸로 해놓고선 오류를 못찾아서 시간 정말 많이 잡아먹음..
'''

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])      # n은 행 개수, m은 열 개수 잊지 말자 ㅠ
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]     # 탐색 방향 상하좌우
    
    queue = deque([(0, 0, 1)])
    
    visited = [[False] * m for _ in range(n)]       # 방문 확인용
    visited[0][0] = True        # 시작점 방문처리
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n - 1 and y == m - 1:       # 도착하면 누적된 거리 리턴
            return distance
        
        for dx, dy in directions:       # 4방향 탐색
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:   # 범위 내, 미방문, '길'이면
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))    # 큐에 추가
                             
    return -1   # 목적지 못가면 -1 리턴