'''
union-find 알고리즘 사용 [경로 압축 기법 Path Compression]
- 여러 개의 원소가 있을 때, 각 원소가 속한 집합을 효율적으로 관리하고, 
- 두 원소가 같은 집합에 속하는지 여부를 빠르게 판단하기 위한 자료구조
- 경로 압축으로 모든 원소가 루트를 가르키는 방법인 경로 압축 기법 사용하여 find보다 연산 속도 훨 빠름 
- rank 사용하여 루트 구분
'''

import sys
input = sys.stdin.readline

def union(a, b):
	rootA = find_parent(a)
	rootB = find_parent(b)

	if rootA != rootB:
		if rank[rootA] > rank[rootB]:
			parent[rootB] = rootA
		elif rank[rootA] < rank[rootB]:
			parent[rootA] = rootB
		else:
			parent[rootB] = rootA
			rank[rootA] += 1


def find_parent(x):
	if parent[x] != x:
		parent[x] = find_parent(parent[x])
	return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)
ans = []
for _ in range(m):
	oper, a, b = map(int, input().split())
	if oper == 0: # 합치기
		union(a,b)
	elif oper == 1: # 포함여부
		if find_parent(a) == find_parent(b):
			ans.append("YES")
		else:
			ans.append("NO")

print("\n".join(ans))
