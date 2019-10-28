less = __import__("check50").import_checks("../less")
from less import *

@check50.check(solve4)
def god_solve4():
    """god mode solves a 4x4 board from starting position"""
    board = ["1", "2", "3", "4",
             "5", "6", "7", "8",
             "9", "10", "11", "12",
             "13", "14", "15", "[_0]"]

    check = check50.run("./fifteen 4")

    check.stdin("GOD", prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("ftw!")

@check50.check(god_solve4)
def god_solve3():
    """god mode solves a 3x3 board after shuffling"""

    # some random valid steps
    steps = ["1","4","7","8","5","2","4","7",
             "3","8","6","5","2","3","6","1",
             "7","6","3","2","5","3","6","4"]

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "[_0]"]

    check = check50.run("./fifteen 4")

    for step in steps:
        check.stdout("Tile to move:")
        check.stdin(step, prompt=False)

    check.stdin("GOD", prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("ftw!")