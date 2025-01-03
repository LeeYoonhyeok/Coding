0. 세그먼트 트리란?
- 세그먼트 트리는 배열의 특정 구간에 대한 연산(합, 최솟값, 최댓값 등)을 빠르게 처리하기 위해 만들어진 자료구조.
- 세그먼트 트리는 배열을 트리 형태로 변환해 구간 연산을 효율적으로 처리.
- 트리 빌드, 구간 쿼리, 값 업데이트를 각각 O(logn) 또는 O(n)에 처리.
- 배열 기반 문제(구간 최솟값, 합 등)를 빠르게 해결할 수 있는 강력한 도구.


1. 왜 세그먼트 트리가 필요한가?
문제 상황: 배열이 있을 때, 다음 작업을 반복적으로 수행해야 한다고 가정합니다:
배열의 특정 구간 [L,R]의 최솟값/최댓값/합을 구하기.
배열의 특정 값을 업데이트하기.
비효율적인 접근:
단순히 반복문으로 [L,R] 범위를 순회하면 한 쿼리당 시간 복잡도는 O(R−L+1)입니다.
쿼리와 업데이트가 많으면 O(n^2)에 가까워져 시간 초과가 발생할 수 있습니다.
세그먼트 트리의 등장: 세그먼트 트리는 배열을 트리 형태로 변환하여, 다음 두 작업을 매우 효율적으로 처리합니다:

특정 구간의 연산 결과를 빠르게 계산 (O(logn)).
배열 값을 업데이트하면서 트리 전체를 자동으로 갱신 (O(logn)).


2. 세그먼트 트리의 구조와 동작

구조
- 세그먼트 트리는 완전 이진 트리입니다.
- 배열의 각 원소는 리프 노드에 저장됩니다.
- 내부 노드는 자식 노드들의 값을 기반으로 특정 구간의 연산 결과(최솟값, 최댓값, 합 등)를 저장합니다.

동작
- 트리 빌드
    - 배열에서 리프 노드를 생성한 후, 내부 노드를 채워나갑니다.
    - 각 내부 노드는 자식 노드의 연산 결과를 저장합니다.

- 구간 쿼리
    - 특정 구간 [L,R]에 대해 연산을 수행할 때, 필요한 노드만 탐색합니다.
    - 전체 배열을 탐색하지 않고 O(logn) 시간에 처리합니다.

- 업데이트
    - 배열의 특정 값을 변경하면, 해당 노드와 관련된 부모 노드들만 갱신합니다.
    - 역시 O(logn)에 처리됩니다.


3. 세그먼트 트리의 예제
배열: [2,1,5,3,4]
세그먼트 트리의 모습 (최솟값 저장):
                 1
              /     \
            1         3
          /   \     /   \
         2     1   5     3
                       /   \
                      4     INF
설명:

리프 노드: 배열의 원소를 저장합니다.

리프 노드는 트리의 가장 아래에 위치합니다.
예: 2, 1, 5, 3, 4.

내부 노드: 자식 노드들의 연산 결과를 저장합니다.
예: min(2,1)=1, min(5,3)=3.

루트 노드: 전체 배열의 연산 결과를 저장합니다.
예: min(1,3)=1.


4. 세그먼트 트리의 구현

- 트리 빌드
트리 빌드는 배열의 구간 정보를 재귀적으로 계산합니다.

배열을 반으로 나눕니다.
왼쪽 구간과 오른쪽 구간의 값을 계산합니다.
부모 노드는 두 구간의 결과를 결합합니다.

def build_segment_tree(data, tree, node, start, end):
    if start == end:  # 리프 노드
        tree[node] = data[start]
    else:  # 내부 노드
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        build_segment_tree(data, tree, left_node, start, mid)
        build_segment_tree(data, tree, right_node, mid + 1, end)
        tree[node] = min(tree[left_node], tree[right_node])

- 구간 쿼리
구간 [L,R]의 값을 찾기 위해 노드를 탐색합니다:

현재 노드가 쿼리 구간에 완전히 포함되면 값을 반환.
현재 노드가 쿼리 구간과 겹치면 자식 노드로 탐색.
현재 노드가 쿼리 구간과 겹치지 않으면 무시.

def query_segment_tree(tree, node, start, end, L, R):
    if R < start or L > end:  # 구간 밖
        return float('inf')
    if L <= start and end <= R:  # 완전히 포함
        return tree[node]
    # 부분적으로 겹침
    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    left_query = query_segment_tree(tree, left_node, start, mid, L, R)
    right_query = query_segment_tree(tree, right_node, mid + 1, end, L, R)
    return min(left_query, right_query)

- 값 업데이트
특정 값을 변경하면, 그 영향을 받는 노드들만 갱신합니다.

def update_segment_tree(data, tree, node, start, end, idx, value):
    if start == end:  # 리프 노드
        data[idx] = value
        tree[node] = value
    else:
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        if start <= idx <= mid:
            update_segment_tree(data, tree, left_node, start, mid, idx, value)
        else:
            update_segment_tree(data, tree, right_node, mid + 1, end, idx, value)
        tree[node] = min(tree[left_node], tree[right_node])


5. 세그먼트 트리의 시간 복잡도
- 트리 빌드: O(n) (배열 전체를 한 번 순회)
- 구간 쿼리: O(logn) (트리의 높이만 탐색)
- 값 업데이트: O(logn) (트리의 높이만 갱신)


6. 직관적으로 이해하기
구간 쿼리란?
예를 들어, 배열에서 [1,3] 구간의 최솟값을 구하려고 합니다.
세그먼트 트리는 이 구간의 값을 트리에서 빠르게 계산합니다.

업데이트란?
배열의 값이 변경되면, 그 영향을 받는 트리의 노드만 갱신합니다.