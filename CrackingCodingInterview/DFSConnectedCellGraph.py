def get_biggest_region(grid):
    # visited_row = [0]*len(grid)
    # visited_row_col = [visited_row]*len(grid[0])
    n = len(grid)
    m = len(grid[0])
    visited_row_col = [[0 for x in range(m)] for y in range(n)]

    print 'original', visited_row_col

    max_count = 0

    for idx_row, point in enumerate(grid):
        for idx_col, point_col in enumerate(grid[idx_row]):
            print "current position", idx_row, idx_col, visited_row_col[idx_row][idx_col]
            if visited_row_col[idx_row][idx_col] ==0:
                cur_count = 0
                stack_to_look = []
                stack_to_look.append([idx_row, idx_col])
                while len(stack_to_look) >0:
                    print 'current stack', stack_to_look
                    to_look = stack_to_look.pop()
                    row = to_look[0]
                    col = to_look[1]
                    visited_row_col[row][col] = 1
                    print 'to_look', to_look, row, col, 'visited row col', visited_row_col
                    print 'in grid', grid[row][col]
                    if grid[row][col] == 1:
                        print 'yes cound!'
                        # increment count
                        print 'current_count', cur_count
                        cur_count += 1
                        # add any surrounding members to stack
                        if idx_row + 1 < n:
                            stack_to_look.append([idx_row + 1, idx_col])
                            if idx_col - 1 >= 0:
                                stack_to_look.append([idx_row + 1, idx_col - 1])
                            if idx_col + 1 < m:
                                stack_to_look.append([idx_row + 1, idx_col + 1])
                        if idx_col + 1 < m:
                            stack_to_look.append([idx_row , idx_col + 1])
                            if idx_row - 1 >=0:
                                stack_to_look.append([idx_row - 1, idx_col + 1])
                        if idx_row - 1 >=0:
                            stack_to_look.append([idx_row - 1, idx_col])
                            if idx_col -1 >=0:
                                stack_to_look.append([idx_row - 1, idx_col -1])
                        if idx_col - 1 >=0:
                            stack_to_look.append([idx_row, idx_col -1])
                        print 'stack after adding', stack_to_look
                    break
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