'''
뱀 구현 문제
deque로 이동했던 위치 삽입, directions을 시계방향으로 설정 후 알맞은 방향에 맞게 설정
while True로 계속 직진하다 X초가 되면 회전

헤맸던 부분
- 시작점으로부터 X초 후에 회전인데, X초 후에 회전으로 설정했던 부분 ㅜ
- 초기 시간 0초로 설정
- 마지막 벽이나 몸 부딪혔을 때 +1초 후 return
'''

import sys
from collections import deque

def snake_game():
    moving_times = 0
    position = deque([(1,1)])
    directions = [(-1,0), (0,1), (1,0), (0,-1)] # 위오아왼 순서
    now_direction = 1 # 초반 오른쪽 방향
    spin_times = 0    
    
    while True:
        x, y = position[-1]
        dx, dy = directions[now_direction]
        x, y = x+dx, y+dy
        
        if not(1 <= x <= N and 1 <= y <= N) or (x,y) in position:
            return moving_times + 1
        
        moving_times += 1
        position.append((x, y)) 
        
        if (x,y) in apples:
            apples.remove((x,y))
        else:
            position.popleft()
            
        if spin_times < L and moving_times == int(movements[spin_times][0]):
            d = movements[spin_times][1]
            if d == 'D': # 오른쪽
                now_direction = (now_direction + 1) % 4
            elif d == 'L': # 왼쪽
                now_direction = (now_direction - 1) % 4
            spin_times += 1            

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
movements = [list(map(str, sys.stdin.readline().split())) for _ in range(L)]
print(snake_game())