'''
단어의 자릿수를 고려해서 가중치를 주는 딕셔너리 생성
가중치 딕셔너리 역정렬 후 순서에 맞게 9부터 0까지 단어 숫자 딕셔너리 생성
그 후 for문을 돌며 답 계산
'''

import sys
input = sys.stdin.readline

def solution(cases): 
    weights = dict()    

    for word in cases:
        length = len(word)
        for i, char in enumerate(word):
            if char not in weights:
                weights[char] = 0
            weights[char] +=  10 ** (length - i - 1)
                    
    sorted_weights = sorted(weights.items(), key = lambda x:x[1], reverse=True)
    
    num = 9
    alpha_to_number = {}
    for char, _ in sorted_weights:
        alpha_to_number[char] = num
        num -= 1
        
    total_value = 0
    for word in cases:
        current_value = ''
        for char in word:
            current_value += str(alpha_to_number[char])
        total_value += int(current_value)
        
    return total_value

N = int(input())
cases = [input().rstrip() for _ in range(N)]
print(solution(cases))
