'''
- dp map에 경우의 수 추가하기
- dp를 2차원으로 만들어서 이전에 어떤 방향으로 들어왔는지 체크 (가로:0, 세로:1, 대각선:2)
- 처음: (0,0), (0,1) 가로방향 시작 (첫시작점은 가로 상태로 (0,1)에서 출발한다고 생각하면 됨)
- (x,y) 좌표에 특정 방향으로 들어오기 위해 이전의 개수를 합치는 방식

- 경우의 수
가로 -> 가로 or 대각선
세로 -> 세로 or 대각선
대각선 -> 세로 or 가로 or 대각선
'''

import sys
input = sys.stdin.readline

def count_movement(N, house):
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1
    for x in range(N):
        for y in range(N):
            if house[x][y] == 1:
                continue
            
            # 가로로 (x,y)에 이동한 경우 : 가로 or 대각선으로 들어옴
            if y >= 1:
                dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
                
            # 세로로 (x,y)에 이동한 경우 : 세로 or 대각선으로 들어옴
            if x >= 1:
                dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]
            
            # 대각선으로 (x,y)에 이동한 경우 : 가로 or 세로 or 대각선으로 들어옴
            if x >= 1 and y >= 1 and house[x][y-1] == 0 and house[x-1][y] == 0:
                dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
                
    return sum(dp[N-1][N-1])
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
print(count_movement(N, house))