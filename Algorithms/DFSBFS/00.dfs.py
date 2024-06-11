# 최대 깊이가 10, 
map = [[0]*10 for _ in range(10)]
map[5,9] = 'target'
dir = [(0,1), (-1,0), (0,-1), (1,0)]  # y, x 

def dfs(level, y, x):
    # 끝날 조건
    if level == 10:
        return 
    
    if map[y][x] == 'target':
        return  
    
    # 순회 
    for i in range(4):
        dy = y + dir[i][0]
        dx = x + dir[i][1]
        
        dfs(level+1, dy, dx)
    
