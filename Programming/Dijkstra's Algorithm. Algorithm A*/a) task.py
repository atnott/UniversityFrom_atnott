import heapq

def getDist(n, m, d, start, finish):
    sx, sy = start
    fx, fy = finish
    visited = [[False] * m for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]
    dist[sx][sy] = 0
    heap = []
    heapq.heappush(heap, (0, sx, sy))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while heap:
        curr_dist, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == fx and y == fy:
            return curr_dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if abs(d[nx][ny] - d[x][y]) <= 100:
                    new_dist = curr_dist + 1
                    if new_dist < dist[nx][ny]:
                        dist[nx][ny] = new_dist
                        heapq.heappush(heap, (new_dist, nx, ny))

n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
start = tuple(map(int, input().split()))
cargo = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))
dist1 = getDist(n, m, d, start, cargo)
dist2 = getDist(n, m, d, cargo, finish)
print(dist1 + dist2)