# 해쉬 함수 적용하기
# 문자열 받아서 for문으로 1씩 늘어날때마다 제곱수 늘리기
# 분명 맞게 한거 같은데 뭐가 틀린지 모르겟음 ;;;
# 누군가가 반례나 설명해주시면 감사 하겠음 ㅜ
L = int(input())
string = input().strip()

def hash_func():
    hash_val = 0
    r = 31
    M = 1234567891
    for i in range(len(string)):
        str_hash = ord(string[i]) - ord('a') +1
        hash_val += str_hash * (r**i)
        hash_val %= M
    return hash_val

