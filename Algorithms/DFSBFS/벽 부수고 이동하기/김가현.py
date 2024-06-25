# 참고 블로그 : https://velog.io/@charmull/%EB%B0%B1%EC%A4%80Python-2206.-%EB%B2%BD-%EB%B6%80%EC%88%98%EA%B3%A0-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-3%EC%B0%A8%EC%9B%90%EC%9C%BC%EB%A1%9C-%ED%92%80%EA%B8%B0

import sys
input = sys.stdin.readline
from collections import deque

# 벽을 부쉈는지를 visited에서 확인 => 3차원 리스트에 담음
# visited[{행}][{열}][{벽을 부순 횟수}] = {총 이동 횟수}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

            if matrix[nx][ny] == 1 and z == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                q.append((nx, ny, 1))

    return -1

print(bfs())
