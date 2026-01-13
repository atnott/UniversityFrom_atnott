import heapq

def manh_dist(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def getDist(n, m, d, start, finish):
    sx, sy = start
    fx, fy = finish
    g_score = [[float('inf')] * m for _ in range(n)]
    g_score[sx][sy] = 0
    visited = [[False] * m for _ in range(n)]
    heap = []
    f_start = manh_dist(sx, fx, sy, fy)
    heapq.heappush(heap, (f_start, 0, sx, sy))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while heap:
        f_score, g_curr, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == fx and y == fy:
            return g_curr
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if abs(d[nx][ny] - d[x][y]) <= 100:
                    new_g = g_curr + 1
                    if new_g < g_score[nx][ny]:
                        g_score[nx][ny] = new_g
                        h = manh_dist(nx, fx, ny, fy)
                        f = new_g + h
                        heapq.heappush(heap, (f, new_g, nx, ny))

n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
start = tuple(map(int, input().split()))
cargo = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))
# 2 3
# 0 1000 0
# 0 0 0
# 0 0
# 0 2
# 1 1
dist1 = getDist(n, m, d, start, cargo)
dist2 = getDist(n, m, d, cargo, finish)
print(dist1 + dist2)
