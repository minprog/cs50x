less = __import__("check50").import_checks("../less")
from less import *


@check50.check(correct_solve_dfs_it)
def generate_sudoku_different():
    """generate_sudoku() generates a different sudoku puzzle each time"""
    module = uva.check50.py.run("sudoku.py").module
    sudokus = [module.generate_sudoku() for i in range(3)]

    for sud1, sud2 in itertools.combinations(sudokus, 2):
        if not is_different(sud1, sud2):
            raise check50.Failure()


@check50.check(generate_sudoku_different)
def generate_sudoku_solvable():
    """generate_sudoku() generates solvable sudokus with at least 30 empty spots"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.generate_sudoku()
    original = copy.deepcopy(sudoku)

    actual = module.solve_dfs_it(sudoku)

    if not isinstance(actual, list):
        actual = sudoku

    check_sudoku(original)
    check_sudoku(actual)

    n_empty = sum(original[x][y] == 0 for x in range(9) for y in range(9))

    if n_empty < 30:
        raise check50.Failure(f"Found only {n_empty} empty spots.")

    check_solved(actual, original)


@check50.check(compiles)
def correct_solve_dfs_gen():
    """solve_dfs_gen() can solve puzzle4"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("hard/puzzle4.sudoku")
    original = copy.deepcopy(sudoku)

    actual = module.solve_dfs_gen(sudoku)
    if not isinstance(actual, list):
        actual = sudoku

    check_sudoku(original)
    check_sudoku(actual)
    check_solved(actual, original)
