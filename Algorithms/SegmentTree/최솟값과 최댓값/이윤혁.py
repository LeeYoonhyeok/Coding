'''
세그먼트 트리 활용
세그먼트 트리는 이진형태. 최댓값과 최솟값을 각 트리 노드에 저장하여 사용

세그먼트 트리는 이진 트리로 트리 높이는 log2(N)임.
따라서 필요한 노드 수는 2^(log2(N)+1)-1개임.
이 노드 수와 4N을 비교하면 어떤 경우에도 초과하지 않음. 그렇기에 4N으로 간단히 설정하고 진행
'''

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)
# 기본 재귀 깊이 제한은 1000 -> 10^8 = 1억번의 재귀 호출 허용

def build_tree(start, end, node):
    if start == end:
        seg_min[node] = arr[start]
        seg_max[node] = arr[start]
        return seg_min[node], seg_max[node]
    
    mid = (start + end) // 2
    left_min, left_max = build_tree(start, mid, node*2)
    right_min, right_max = build_tree(mid+1, end, node*2+1)
    
    seg_min[node] = min(left_min, right_min)
    seg_max[node] = max(left_max, right_max)
    return seg_min[node], seg_max[node]


def query(start, end, node, left, right):
    if right < start or left > end: # 범위 밖
        return float('inf'), float('-inf')
    
    if left <= start and end <= right : # 구간 온전히 포함
        return seg_min[node], seg_max[node]
    
    # 구간이 걸쳐 있을 때 좌/우로 분할 탐색
    mid = (start + end) // 2
    left_min, left_max = query(start, mid, node * 2, left, right)
    right_min, right_max = query(mid+1, end, node*2+1, left, right)
    
    return min(left_min, right_min), max(left_max, right_max)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

seg_min = [0] * (4 * n)
seg_max = [0] * (4 * n)

build_tree(0, n-1, 1)

results = []
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    min_value, max_value = query(0, n-1, 1, a, b)
    results.append(f"{min_value} {max_value}")
    
print("\n".join(results))    