'''
수빈이가 이동하려 하는 채널 N의 최댓값은 500,000임.
따라서 전체 탐색으로 0부터 목표 채널인 N + 최댓값인 500001을 더한 범위를 탐색
'''
import sys
input = sys.stdin.readline

def is_possible(channel, broken):
    for num in str(channel):
        if int(num) in broken:
            return False
    return True    

def min_click(N, broken):
    current_channel = 100
    min_clicks = abs(N - current_channel)
    
    for channel in range(N + 500001):
        if is_possible(channel, broken):
            clicks = len(str(channel)) + abs(channel-N)
            min_clicks = min(min_clicks, clicks)
    
    return min_clicks

N = int(input())
M = int(input())
broken = list(map(int, input().split())) if M > 0 else []

print(min_click(N, broken))



