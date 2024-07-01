from queue import Queue
def solution(maps):
    answer = -1
    q = Queue()
    q.put((0, 0, 1))
    n, m = len(maps), len(maps[0])

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True 
    while not q.empty():
        y, x, dit = q.get() 

        if (y == (n - 1)) & (x == (m - 1)):
            answer = dit
            break 

        for i in range(4):
            dy = y + dir[i][0]
            dx = x + dir[i][1]

            if (dy < 0) | (dx < 0) | (dy >= n) | (dx >= m):
                continue 
            
            if maps[dy][dx] == 0:
                continue 

            if visited[dy][dx]:
                continue

            visited[dy][dx] = True
            q.put((dy, dx, dit + 1))

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))