'''
0위치에 벽을 3개 세울 수 있음
-> 벽을 세울 좌표 조합 구하기
-> 각 조합에 따라 안전 영역 최댓값 구하기
바이러스 퍼지게 하는 함수
-> 벽 세운 후의 map이 들어와야 함
안전 영역 개수 확인 함수

'''
from collections import deque
from itertools import combinations
import sys, copy


def solution(lab, n, m):
    empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
    max_safe_area = 0
    
    for walls in combinations(empty_spaces, 3):
        new_lab = copy.deepcopy(lab)
        for x, y in walls:
            new_lab[x][y] = 1
        spread_virus(new_lab, n, m)
        max_safe_area = max(max_safe_area, count_safe_area(new_lab))
        
    return max_safe_area

def count_safe_area(lab):
    return sum(row.count(0) for row in lab)

def spread_virus(lab, n, m):
    dirs = [(0,1), (0,-1), (-1,0), (1,0)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx,ny))

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(solution(lab, N, M))