import check50
import check50.flask
import re


def is_hardcoded(text):
    """check if a string is hardcoded"""
    regex = r"(.*)"

    for word in text.split():
        regex += word + "(.*|\n)"

    with open("bleep.py") as file:
        file_content = file.read()
        match = re.search(regex, file_content, re.IGNORECASE | re.DOTALL)

        if match:
            return True
        
    return False


@check50.check()
def exists():
    """bleep exists"""
    check50.exists("bleep.py")
    check50.include("banned.txt", "banned2.txt")


@check50.check(exists)
def test_reject_no_args():
    """rejects len(sys.argv) less than 2"""
    check50.run("python3 bleep.py").exit(1)


@check50.check(exists)
def test_reject_many_args():
    """rejects len(sys.argv) more than 2"""
    check50.run("python3 bleep.py banned.txt banned.txt").exit(1)


@check50.check(exists)
def test_no_banned_words():
    """input of 'hello world' outputs 'hello world'"""
    check50.run("python3 bleep.py banned.txt").stdin("Hello world").stdout("Hello world\s*\n", "Hello world\n").exit(0)


@check50.check(exists)
def test_darn():
    """input of 'This darn world' outputs 'This **** world'"""
    check50.run("python3 bleep.py banned.txt").stdin("This darn world").stdout("This \*\*\*\* world\s*\n", "This **** world\n").exit(0)


@check50.check(exists)
def handles_capitalized():
    """input of 'THIS DARN WORLD' outputs 'THIS **** WORLD'"""
    check50.run("python3 bleep.py banned.txt").stdin("THIS DARN WORLD").stdout("THIS \*\*\*\* WORLD\s*\n", "THIS **** WORLD\n").exit(0)


@check50.check(test_darn)
def darn_not_hardcoded():
    """input of 'This darn world' and 'THIS DARN WORLD' are not hardcoded"""
    hardcoded = is_hardcoded('This darn world')

    if hardcoded:
        raise check50.Failure("Don't hardcode for check50!")


@check50.check(exists)
def substrings():
    """doesn't censor substrings"""
    check50.run("python3 bleep.py banned.txt").stdin("Darning my socks").stdout("Darning my socks\s*\n", "Darning my socks\n").exit(0)


@check50.check(substrings)
def substrings_not_hardcoded():
    """input of 'Darning my socks' is not hardcoded"""
    hardcoded = is_hardcoded('Darning my socks')

    if hardcoded:
        raise check50.Failure("Don't hardcode for check50!")


@check50.check(exists)
def handles_other_wordlists():
    """handles banned words lists with arbitrary words in them"""
    check50.run("python3 bleep.py banned2.txt").stdin("My cat and dog are great").stdout("My \*\*\* and \*\*\* are great\s*\n", "My *** and *** are great\n").exit(0)


@check50.check(handles_other_wordlists)
def other_wordlists_not_hardcoded():
    """input of 'My cat and dog are great' is not hardcoded"""
    hardcoded = is_hardcoded('My cat and dog are great')

    if hardcoded:
        raise check50.Failure("Don't hardcode for check50!")
