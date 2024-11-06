'''
치킨집(2)을 기준으로 치킨거리 계산
-> 집을 기준으로 치킨집 여러개 있을 때 치킨거리를 계산
-> 이전에 m개의 치킨집을 combination으로 조합 후 판단
'''
from itertools import combinations
import sys

def solution(maps, n, m):
    chickens = [(i+1,j+1) for i in range(n) for j in range(n) if maps[i][j] == 2]
    houses = [(i+1,j+1) for i in range(n) for j in range(n) if maps[i][j] == 1]
    min_chicken_dist = float('inf')
    for combi in combinations(chickens, m):
        min_chicken_dist = min(min_chicken_dist, find_chicken_dist(combi, houses))
 
    return min_chicken_dist

def find_chicken_dist(chickens, houses):
    chicken_dist = 0
    for hx, hy in houses:
        dist = float('inf')
        for cx, cy in chickens:
            dist = min(dist, (abs(cx-hx) + abs(cy-hy)))
        chicken_dist += dist
        
    return chicken_dist
N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(maps, N, M))