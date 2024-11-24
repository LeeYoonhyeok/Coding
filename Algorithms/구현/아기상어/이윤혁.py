'''
아기 상어가 물고기를 잡아먹을 수 있는 시간 출력
처음 아기상어의 크기는 2, 1초에 상하좌우로 한 칸씩 이동
자신보다 큰 물고기 지나갈 수 없음
자신보다 작은 물고기 먹을 수 있음
가장 가까운 물고기를 먹으러감. 위쪽 & 왼쪽 우선 -> 상좌하우로 이동
자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가
완전 탐색 후 dist순으로 정렬 -> 첫번째 물고기 먹기 -> 다 먹을 떄까지 반복
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, start, size):
    directions = [(-1,0), (0,-1), (1,0), (0,1)] #상좌하우
    visited = [[False] * N for _ in range(N)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    fish_list = []
    
    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if spaces[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
                    if 0 < spaces[nx][ny] < size:
                        fish_list.append((dist+1, nx, ny))
    
    return sorted(fish_list)[0] if fish_list else None

N = int(input())
spaces = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if spaces[i][j] == 9:
            shark_pos = (i, j)
            spaces[i][j] = 0
            
shark_size = 2
shark_eaten = 0
time = 0

while True:
    result = bfs(N, shark_pos, shark_size)
    if not result:
        break
    
    dist, nx, ny = result
    time += dist
    shark_eaten += 1
    spaces[nx][ny] = 0
    shark_pos = (nx, ny)
    
    if shark_eaten == shark_size:
        shark_size += 1
        shark_eaten = 0

print(time)