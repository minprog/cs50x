less = __import__("check50").import_checks("../less")
from less import *

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
