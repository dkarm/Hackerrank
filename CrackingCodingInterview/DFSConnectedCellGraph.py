def get_biggest_region(grid):
    n = len(grid)
    m = len(grid[0])
    visited_row_col = [[0 for x in range(m)] for y in range(n)]
    max_count = 0

    for idx_row, point in enumerate(grid):
        for idx_col, point_col in enumerate(grid[idx_row]):
            if visited_row_col[idx_row][idx_col] == 0:
                cur_count = 0
                stack_to_look = []
                stack_to_look.append([idx_row, idx_col])
                while len(stack_to_look) > 0:
                    to_look = stack_to_look.pop()
                    row = to_look[0]
                    col = to_look[1]
                    if visited_row_col[row][col] == 0 and grid[row][col] == 1:
                        visited_row_col[row][col] = 1
                        cur_count += 1
                        if row + 1 < n and visited_row_col[row + 1][col] == 0:
                            stack_to_look.append([row + 1, col])
                        if row + 1 < n and col - 1 >= 0 and visited_row_col[row + 1][col - 1] == 0:
                            stack_to_look.append([row + 1, col - 1])
                        if row + 1 < n and col + 1 < m and visited_row_col[row + 1][col + 1] == 0:
                            stack_to_look.append([row + 1, col + 1])
                        if col + 1 < m and visited_row_col[row][col + 1] == 0:
                            stack_to_look.append([row, col + 1])
                        if col + 1 < m and row - 1 >= 0 and visited_row_col[row - 1][col + 1] == 0:
                            stack_to_look.append([row - 1, col + 1])
                        if row - 1 >= 0 and visited_row_col[row - 1][col] == 0:
                            stack_to_look.append([row - 1, col])
                        if row - 1 >= 0 and col - 1 >= 0 and visited_row_col[row - 1][col - 1] == 0:
                            stack_to_look.append([row - 1, col - 1])
                        if col - 1 >= 0 and visited_row_col[row][col - 1] == 0:
                            stack_to_look.append([row, col - 1])
                if cur_count > max_count:
                    max_count = cur_count
    return max_count


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)

print get_biggest_region(grid)
