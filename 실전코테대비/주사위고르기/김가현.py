'''
1. N/2 개를 선택하는 조합 구하기
2. 조합 후 합산 비교 -> 내림차순 정렬
3. 최대 승리 횟수, 조합 업데이트
완전탐색 or 이분탐색..?
'''
from itertools import product, combinations
from bisect import bisect_left


def solution(dice):
    answer = []

    aidx = []
    bidx = []

    n = len(dice)
    didx = list(range(len(dice)))  # 주사위 인덱스

    comb = list(combinations(didx, n // 2))  # 조합 경우의 수

    for c in comb:
        aidx.append(list(c))
        # aidx에 포함되지 않은 인덱스 추가
        bidx.append(list(set(didx).difference(c)))

    max_win = 0
    best_combination = []

    for i in range(len(aidx)):
        win = 0
        a_dice = []
        b_dice = []

        for j in aidx[i]:
            a_dice.append(dice[j])
        for j in bidx[i]:
            b_dice.append(dice[j])

        # 모든 가능한 조합의 합
        a_sum = [sum(p) for p in product(*a_dice)]
        b_sum = [sum(p) for p in product(*b_dice)]

        # 이분 탐색

        # 완전 탐색 : 시간 초과 -> 이분 탐색
    #         for a in a_sum:
    #             for b in b_sum:
    #                 if a > b:
    #                     win += 1

    #         if win > max_win:
    #             max_win = win
    #             best_combination = aidx[i]

    answer = [x + 1 for x in best_combination]

    return answer


