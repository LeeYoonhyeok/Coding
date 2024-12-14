import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])        
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def check_available(n, graph, plan):
    parent = [i for i in range(n)]
    rank = [0] * n
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(parent, rank, i, j)
                
    root = find(parent, plan[0]-1)
    for place in plan:
        if find(parent, place-1) != root:
            return 'NO'
    return 'YES'

N = int(input()) # 도시 개수
M = int(input()) # 여행 계획 도시 개수
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
print(check_available(N, graph, plan))
