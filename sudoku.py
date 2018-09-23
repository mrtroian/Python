def check_columns(puzzle, n, nb, alt = 0):
    generateur = range(9) if not alt else reversed(range(9))
    for m in generateur:
        if puzzle[m][n] is nb:
            return False
    return True

def check_squares(puzzle, m, n, nb, alt = 0):
    m -= m % 3
    n -= n % 3
    generateur = range(3) if not alt else reversed(range(3))
    for i in generateur:
        for j in generateur:
            if puzzle[m+i][n+j] is nb:
                return False
    return True

def empty(puzzle):
    for m in puzzle:
        if 0 in m:
            return (puzzle.index(m), m.index(0))
    return False

def allowed(puzzle, m, n, nb, alt = 0):
    if puzzle[m][n] is 0:
        result = not nb in puzzle[m] and check_columns(puzzle, n, nb, alt) and check_squares(puzzle, m, n, nb, alt)
        return result  
    return False

def validateur(puzzle):
    if len(puzzle) is not 9:
        return False
    for m in puzzle:
        if len(m) is not 9:
            return False
    for m in puzzle:
        for n in m:
            if n not in range(10):
                return False
    return True

def solve(puzzle, alt):
    coords = empty(puzzle)
    generateur = range(1, 10) if not alt else reversed(range(1, 10))
    if not coords:
        return True
    for nb in generateur:
        if allowed(puzzle, coords[0], coords[1], nb, alt):
            puzzle[coords[0]][coords[1]] = nb
            if solve(puzzle, alt) and [[0 in m] for m in puzzle]:
                return True
            puzzle[coords[0]][coords[1]] = 0
    return False

def sudoku_solver(puzzle):
    if validateur(puzzle):
        solve(puzzle, False)
    else:
        raise InvalidGrid('Invalid grid')
    return puzzle

def print_grid(puzzle):
    for m in puzzle:
        for n in m:
            print(n, end=' ')
        print()

hard_pzl = [[8,6,0,0,2,0,0,0,0],
            [0,0,0,7,0,0,0,5,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,6,0,8,0,0],
            [0,4,0,0,0,0,0,0,0],
            [0,0,5,3,0,0,0,0,7],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,6,0,0],
            [0,0,7,5,0,9,0,0,0]]

easy_pzl = [[0,0,6,1,0,0,0,0,8], 
            [0,8,0,0,9,0,0,3,0], 
            [2,0,0,0,0,5,4,0,0], 
            [4,0,0,0,0,1,8,0,0], 
            [0,3,0,0,7,0,0,4,0], 
            [0,0,7,9,0,0,0,0,3], 
            [0,0,8,4,0,0,0,0,6], 
            [0,2,0,0,5,0,0,8,0], 
            [1,0,0,0,0,2,5,0,0]]


print_grid(sudoku_solver(easy_pzl))
