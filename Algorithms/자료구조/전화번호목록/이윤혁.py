'''
문자열 sort를 생각해보면, 사전순 정렬 처리로 문자열의 앞부분부터 차례로 비교하여 정렬함.
자릿수 상관없이 문자열의 첫 번째 문자열부터 차례로 유니코드로 비교함.
ex) 1899 199 1999 순서로 정렬
즉, 문자열 정렬은 사전순으로 이루어지며, 접두사 관계에 있는 문자열이 반드시 인접하게 위치하는 것.
'''

import sys
input = sys.stdin.readline

def check_phone_numbers(phone_numbers, n):
    phone_numbers.sort()
    for i in range(n-1):
        if phone_numbers[i] == phone_numbers[i+1][:len(phone_numbers[i])]:
            return 'NO'
    return 'YES'

tc = int(input())
for _ in range(tc):
    n = int(input())
    phone_numbers = []
    for _ in range(n):    
        number = input().rstrip()
        phone_numbers.append(number)
    print(check_phone_numbers(phone_numbers, n))