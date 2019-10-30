import re

less = __import__("check50").import_checks("../less")
from less import *

@check50.check(solve4)
def god_solve4():
    """god mode solves a 4x4 board from starting position."""
    board = " *1 *2 *3 *4 *\\n\\n *5 *6 *7 *8 *\\n\\n *9 *10 *11 *12 *\\n\\n *13 *14 *15 *\_ *\\n\\n *ftw\! *\\n"

    # at least one of the below must be reached at some point
    intermediate_1 = " *1 *2 *3 *4 *\\n\\n *5 *6 *7 *8 *\\n\\n *9 *10 *11 *12 *\\n\\n *13 *14 *\_ *15 *\\n\\n *ftw\! *\\n"
    intermediate_2 = " *1 *2 *3 *4 *\\n\\n *5 *6 *7 *8 *\\n\\n *9 *10 *11 *\_ *\\n\\n *13 *14 *15 *12 *\\n\\n *ftw\! *\\n"

    # run god mode and get output
    check = check50.run("./fifteen 4")
    check.stdin("GOD", prompt=False)
    output = str(check.stdout(timeout=30))

    # compare output with resolved board
    regex = re.compile(board)
    if not regex.search(output):
        raise check50.Failure("didn't find resolved board in output.")

    # check if intermediate steps are also printed
    intermediate_regex_1 = re.compile(intermediate_1)
    intermediate_regex_2 = re.compile(intermediate_2)
    if not intermediate_regex_1.search(output) and not intermediate_regex_2.search(output):
        raise check50.Failure("intermediate steps weren't printed.")

@check50.check(god_solve4)
def god_solve3():
    """god mode solves a 3x3 board after shuffling."""

    # some random valid moves
    steps = ["1","4","7","8","5","2","4","7",
             "3","8","6","5","2","3","6","1",
             "7","6","3","2","5","3","6","4"]

    board = " *1 *2 *3 *\\n\\n *4 *5 *6 *\\n\\n *7 *8 *\_ *\\n\\n *ftw\! *\\n"

    check = check50.run("./fifteen 4")

    # apply random steps
    for step in steps:
        check.stdout("Tile to move:")
        check.stdin(step, prompt=False)

    # run god mode and get output
    check.stdin("GOD", prompt=False)
    output = str(check.stdout(timeout=30))
    
    # compare output with resolved board
    regex = re.compile(board)
    if not regex.search(output):
        raise check50.Failure("didn't find resolved board in output.")