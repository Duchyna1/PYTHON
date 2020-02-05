from random import randint, shuffle

attempts = 5
counter = 1


def make(grid):
    global attempts, counter

    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def checkGrid(grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    return False
        return True

    def solveGrid(grid):
        global counter
        for i in range(0, 81):
            row = i//9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    if not(value in grid[row]):
                        if value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    counter += 1
                                    break
                                else:
                                    if solveGrid(grid):
                                        return True
                break
        grid[row][col] = 0

    def fillGrid(grid):
        global counter
        counter = 1
        for i in range(0, 81):
            row = i//9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(numberList)
                for value in numberList:
                    if not(value in grid[row]):
                        if value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    return True
                                else:
                                    if fillGrid(grid):
                                        return True
                break
        grid[row][col] = 0

    fillGrid(grid)

    while attempts > 0:
        row = randint(0, 8)
        col = randint(0, 8)
        while grid[row][col] == 0:
            row = randint(0, 8)
            col = randint(0, 8)
        backup = grid[row][col]
        grid[row][col] = 0

        copyGrid = []
        for r in range(0, 9):
            copyGrid.append([])
            for c in range(0, 9):
                copyGrid[r].append(grid[r][c])

        counter = 0
        solveGrid(copyGrid)
        if counter != 1:
            grid[row][col] = backup
            attempts -= 1
    return grid


def checkGrid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True
