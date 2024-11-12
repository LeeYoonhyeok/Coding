'''
1광년을 출발로 -1, +1 광년씩 이동 가능
1 -> (0,1광년 이동 가능), 2 -> (1,2,3광년 이동 가능)
처음과 끝은 무조건 1광년 이동
이동 횟수의 최소값을 구하라..

그림 그려보며 dist와 횟수의 도표를 그려봐야 풀리는 문제
작동횟수가 홀수일 때마다 반복되는 횟수 증가
1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9 9 10 10 10 10 10 ... 이런식
'''

import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    x, y = map(int, sys.stdin.readline().split())    
    cnt = 0
    moving_dist = 0
    repeat_cnt = 0
    dist = y - x
    
    while moving_dist < dist:
        cnt += 1
        if cnt % 2 != 0:
            repeat_cnt += 1
        moving_dist += repeat_cnt
        
    print(cnt)
            
            