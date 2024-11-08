'''
d -> 0:북, 1:동, 2:남, 3:서

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    2-1.바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2-2.바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    3-1.반시계 방향으로 90도 회전한다.
    3-2.바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3-3.1번으로 돌아간다.

maps -> 0: 청소안됨, 1: 벽, (?)2: 청소함
'''

import sys


def solution(maps, n, m, i, j, d):
    cnt_clean = 0
    directions = [(-1,0), (0,1), (1,0), (0,-1)] # 0:북, 1:동, 2:남, 3:서
    
    while True:
        if maps[i][j] == 0: # 1번
            maps[i][j] = 2
            cnt_clean += 1
            
        check_cleanable = False
        for _ in range(4):            
            d = (d+3) % 4 # 반시계
            ni, nj = i + directions[d][0], j + directions[d][1]
            
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 0:
                i, j = ni, nj
                check_cleanable = True
                break
            
        if not check_cleanable:
            back_d = (d+2) % 4
            bi, bj = i + directions[back_d][0], j + directions[back_d][1]
            
            if 0 <= bi < n and 0 <= bj < m:
                if maps[bi][bj] == 1:
                    break
                else:
                    i, j = bi, bj
    
    return cnt_clean
    
N, M = map(int, sys.stdin.readline().split())
i,j,d = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(maps, N, M, i, j, d))