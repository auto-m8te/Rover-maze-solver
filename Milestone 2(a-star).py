def a_star(maze):
    rows, cols = 10, 10
    visited = [[False]*cols for _ in range(rows)]
    parent = [[None]*cols for _ in range(rows)]
    g_score = [[float('inf')]*cols for _ in range(rows)]
    f_score = [[float('inf')]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [start]
    g_score[start[0]][start[1]] = 0
    f_score[start[0]][start[1]] = heuristic(start, end)

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_set:
        current = min(open_set, key=lambda p: f_score[p[0]][p[1]])
        if current == end:
            path = []
            x, y = end
            while (x, y) != start:
                path.insert(0, (x, y))
                x, y = parent[x][y]
            path.insert(0, start)
            return path

        open_set.remove(current)
        x, y = current
        visited[x][y] = True

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in ('O', 'E'):
                tentative_g = g_score[x][y] + 1
                if tentative_g < g_score[nx][ny]:
                    parent[nx][ny] = (x, y)
                    g_score[nx][ny] = tentative_g
                    f_score[nx][ny] = tentative_g + heuristic((nx, ny), end)
                    if not visited[nx][ny]:
                        open_set.append((nx, ny))
    return None

maze = [
    ['S', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O'],
    ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X'],
    ['O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X'],
    ['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'E']
]

path = a_star(maze)

if path:
    print("Shortest path:")
    for step in path:
        print(step, end=' ')
else:
    print("No path found.")
