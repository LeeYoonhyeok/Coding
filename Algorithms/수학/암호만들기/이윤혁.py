'''
최소 한 개의 모음 (a,e,i,o,u)
문자열 만들고 [a,e,i,o,u] 개수 구한 후 자음의 개수도 구하기
최소 두 개의 자음
'''
import sys
from itertools import combinations

def solution(alphabets):
    m_li = ['a', 'e', 'i', 'o', 'u']
    alphabets.sort()
    for combi in combinations(alphabets, L):
        m_cnt = sum(1 for char in combi if char in m_li)
        if m_cnt >= 1 and L-m_cnt >= 2:
            print("".join(map(str, combi)))

L, C = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))
solution(alphabets)