import sys
input = sys.stdin.readline

def build_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_tree(arr, tree, node * 2, start, mid)
        build_tree(arr, tree, node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def update_tree(tree, node, start, end, idx, value):
    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_tree(tree, node * 2, start, mid, idx, value)
        else:
            update_tree(tree, node * 2 + 1, mid + 1, end, idx, value)
            
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def query_tree(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    left_sum = query_tree(tree, node * 2, start, mid, left, right)
    right_sum = query_tree(tree, node * 2 + 1, mid + 1, end, left, right)
    
    return left_sum + right_sum
    
n, m, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
results = []
tree = [0] * (4 * n)
build_tree(arr, tree, 1, 1, n)

for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1: # update
        update_tree(tree, 1, 1, n, b, c)
    elif a == 2: # sum
        results.append(query_tree(tree, 1, 1, n, b, c))
        
print("\n".join(map(str, results)))
