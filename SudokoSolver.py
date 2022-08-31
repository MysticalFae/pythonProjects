
def findNextEmpty(puzzle):
    # finds next row, col that's not filled
    # 0 - 8 r the index thing

    for r in range(9): # 0 - 8
        for c in range(9): # 0 - 8
            if puzzle[r][c] == -1: # if space = -1, then it's empty
                return r, c # will return that space

    return None, None # if it's gone through the whole puzzle and there's no -1,
    # then nothing is empty, so return None (special value?)

def isValid(puzzle, guess, row, col):
    # valid? return true, not? return false
    # start with row
    rowVals = puzzle[row] # checks the current row for the value
    if guess in rowVals:
        return False # ie. not valid
    # next collums
    colVals = [puzzle[i][col] for i in range(9)]
    # colVals = []
    #
    # for i in range(9): # I don't exactly understand
    #     colVals.append(puzzle[i][col]) # I think i = row
    #     # so we append (ie. copy) the value of the row spot amd the col sport to colVa;s

    if guess in colVals:
        return False

    # 3 by 3 matrix.. tricky
    # find starting index and col of it
    rowStart = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1... * 3 to get actual index?
    # from this ^^ you can figure out of it's in the 1st set of three rows, second, etc.
    colStart = (col // 3) * 3
    # so I think // means divide and get rid of the remainder / give int
    for r in range(rowStart, rowStart + 3): # starting row plus three
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False

    # if has passed everything else, then it's valid
    return True


def solveSudoku(puzzle):
    # uses backtracking
    # puzzle = a lists of list, blank spaces are -1s
    # trying to see if it's sovle-able

    #choose somewhere on board to make a guess

    row, col = findNextEmpty(puzzle)

    # if no row left, validation checks

    if row is None:
        return True # we solved puzzle

    # if place, then come up with guess between 1-9

    for guess in range(1, 10): # the possible numbers on the puzzle
        # check if valid guess
        if isValid(puzzle, guess, row, col):
            # place the guess on the puzzle if true
            puzzle[row][col] = guess
            #mutating puzzle
            # recursively call our function
            if solveSudoku(puzzle):
                return True

            # if not valid or does not solve
            # back track, guess was wrong

        puzzle[row][col] = -1  # resetting it to empty

        # so if it's unsovable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(example_board))
    print(example_board)

