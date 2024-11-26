'''
분할정복 알고리즘
시간복잡도 O(N^3 * B) -> O(N^3 * logB)로 줄임
B가 매우 클 때 시간복잡도가 상당히 커지므로 분할정복 사용
B가 홀수일 때 A^(2k+1) = A^k * A^k * A
B가 짝수일 때 A^2k = A^k * A^k
그러므로 홀수일 때는 result를 따로 만들어 A만 곱해주고, A행렬에는 계속해서 A를 곱함
마지막에 B가 1일 때에도 홀수이므로 result에 A를 곱해주면서 결과를 반환
'''

import sys
input = sys.stdin.readline

def matrix_mul(A,B,mod=1000):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n): # A row index`
        for j in range(n): # B col index
            for k in range(n): # A col index & B row index
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def matrix_pow(A,B, mod=1000):
    n = len(A)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while B > 0:
        if B % 2 == 1:
            result = matrix_mul(result, A, mod)
        A = matrix_mul(A,A,mod)
        B //= 2
    return result

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = matrix_pow(matrix, B)
for row in result:
    print(" ".join(map(str, row)))