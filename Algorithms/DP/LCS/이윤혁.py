'''
LCS 최장 공통 부분 수열 구하기
DP문제이기에 prev, curr 배열 만든 후 2중 포문으로 문자열 비교하며 dp list 업데이트
'''

import sys
def LCS(str1, str2):
    len1, len2 = len(str1), len(str2)
    prev = [0] * (len2 + 1)
    curr = [0] * (len2 + 1)
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, [0] * (len2 + 1)
    return prev[-1]

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
print(LCS(str1, str2))