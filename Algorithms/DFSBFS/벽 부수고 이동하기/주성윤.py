# 1. 최단경로 문제 (bfs)
# 2. 0가 통로, 1이 벽
# 3. 벽을 한개까지 부수고 이동할 수 있음
# 벽 부수는 것을 어떻게 카운팅할 것인가?
# visited 함수를 쓸 때, 3차원으로 두고, visited[0][0][0]이면 안부수고 방문, [0][0][1]이면 부수고 방문으로 가정
# 게임맵 최단거리 코드 참고
# 28번 라인부터 경우의 수 체크가 헷갈려서 인공지능 참고
# 내일 다시 복습
from collections import deque

n,m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]

def is_valid_move(n,m,dx,dy):
    return 0 <= dx < n and 0 <= dy < m

def bfs(n,m,maps):
    dir = [(0,1),(-1,0),(0,-1),(1,0)]
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    queue = deque([(0,0,0,1)]) # x,y,crash,cnt
    visited[0][0][0] = True
    while queue:
        x,y,crash,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            dx, dy = x + dir[i][0], y + dir[i][1]
            if is_valid_move(n,m,dx,dy):
                if maps[dx][dy] == 0 and not visited[dx][dy][crash]: # 통로이고, 방문도 안했다면
                    queue.append((dx,dy,crash,cnt+1))
                    visited[dx][dy][crash] = True
                elif maps[dx][dy] == 1 and crash == 0 and not visited[dx][dy][1]: # 벽이지만 아직 안부셨고 방문도 안했다면
                    queue.append((dx,dy,1,cnt+1))
                    visited[dx][dy][1] = True
    return -1
            
def solution():
    print(bfs(n,m,maps))
solution()