def solve(grid):
    def print_grid(arr):
        for y in range(9):
            for x in range(9):
                print(arr[x][y], end=' ')
            print('')

    def empty_spot(arr, l):
        for row in range(9):
            for col in range(9):
                if(arr[row][col] == 0):
                    l[0] = row
                    l[1] = col
                    return True
        return False

    def used_in_row(arr, row, num):
        for i in range(9):
            if(arr[row][i] == num):
                return True
        return False

    def used_in_col(arr, col, num):
        for i in range(9):
            if(arr[i][col] == num):
                return True
        return False

    def used_in_box(arr, row, col, num):
        for i in range(3):
            for j in range(3):
                if(arr[i+row][j+col] == num):
                    return True
        return False

    def legit(arr, row, col, num):
        return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num) 

    def solve_sudoku(arr):
        l = [0, 0]
        if(not empty_spot(arr, l)):
            return True
        row = l[0]
        col = l[1]
        for num in range(1, 10):
            if(legit(arr, row, col, num)):
                arr[row][col] = num
                if(solve_sudoku(arr)):
                    return True
                arr[row][col] = 0
        return False

    if(solve_sudoku(grid)):
        print('\nHELP')
        print_grid(grid)
        return grid
    else:
        print("No solution exists")
