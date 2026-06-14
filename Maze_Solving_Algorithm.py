def a_star_search(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Find start and end positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        return "Invalid maze: Missing start or end."

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manh-attan Distance

    # Manually managed priority queue (sorted list instead of heapq)
    open_set = [(0, start)]  # (cost, position)
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        open_set.sort()  # Keep list sorted to get the lowest cost first
        _, current = open_set.pop(0)  # Get node with lowest f_score

        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return list(reversed(path))

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != 'X':
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)

                    # Add to open_set, ensuring it's always sorted
                    open_set.append((f_score[neighbor], neighbor))

    return "No path found."
