'''
유니온 파인드 문제
해당 문제는 n,m 이 제한적이고 participants[0]을 기준으로 연결되므로 자연스레 균형을 이루는 구조
그렇기 때문에 rank를 사용하지 않고 경로 압축으로만 표현하는 것이 효율적
'''

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth_set = set(truth[1:])

parent = [i for i in range(n+1)]
parties = []

# 각 파티에 참여하는 사람들의 정보 저장 및 유니온
for _ in range(m):
    party = list(map(int, input().split()))
    party_size = party[0]
    participants = party[1:]
    parties.append(participants)
    for i in range(1, len(participants)):
        union(parent, participants[0], participants[i])

# 진실을 아는 사람들의 최상위 부모 찾기
truth_roots = set()
for person in truth_set:
    truth_roots.add(find(parent, person))

# 각 파티에 대해 진실을 아는 사람이 포함되어 있는지 확인
count = 0
for participants in parties:
    is_safe = True
    for person in participants:
        if find(parent, person) in truth_roots:
            is_safe = False
            break
    if is_safe:
        count += 1

print(count)
