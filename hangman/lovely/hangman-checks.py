import check50
import os
import sys
import random
import string

def raise_timeout():
    raise Exception("Timeout")

@check50.check()
def exists():
    """hangman.py exists"""
    check50.exists("hangman.py")
    check50.include("dictionary.txt")

@check50.check(exists, timeout=3)
def can_import():
    """hangman.py loads without printing anything"""
    res = check50.run('python3 -c "import hangman"').stdout(timeout=2)
    if res != "":
        raise check50.Failure("Code produced output when imported.", 
            help='Did you wrap all code except the classes in ' \
                    '"if __name__ == \'__main__\'"?')

@check50.check(can_import)
def load_lexicon():
    """lexicon object can be created"""
    sys.path.append(os.getcwd())
    import hangman
    try:
        Lexicon = hangman.Lexicon
        lex = Lexicon()
    except Exception as e:
        error='unable to create a lexicon object using "Lexicon()"'
        help=f"got exception {str(e)}."
        raise check50.Failure(error, help=help)

@check50.check(load_lexicon)
def test_lexicon():
    """lexicon object correctly extracts 4-letter words from dictionary.txt"""
    sys.path.append(os.getcwd())
    import hangman
    Lexicon = hangman.Lexicon
    lex = Lexicon()

    try:
        words = lex.get_words(4)
    except Exception as e:
        raise check50.Failure('unable to get words of length 4 from lexicon '\
            'object with "lex.get_words(4)"')

    if len(words) != 4128:
        raise check50.Failure("did not succesfully load all 4-letter words",
                help=f"expected 4128 words, got {len(words)}")

@check50.check(can_import)
def load_hangman():
    """creating a hangman game with parameters length=4, guesses=5 succeeds"""
    sys.path.append(os.getcwd())
    import hangman
    try:
        Hangman = hangman.Hangman
    except Exception as e:
        raise check50.Failure("cannot find the Hangman class")

    try:
        game = Hangman(4, 5)
    except Exception as e:
        raise check50.Failure("failed to create a Hangman object for a " \
                "length 4 word and 5 guesses",
                help=f"got exception {e}.")

@check50.check(load_hangman)
def empty_game():
    """finished, won and lost respond correctly for a brand new game"""
    sys.path.append(os.getcwd())
    import hangman
    Hangman = hangman.Hangman
    game = Hangman(4, 5)
    try:
        finished = game.finished()
        won = game.won()
        lost = game.lost()
    except Exception as e:
        raise check50.Failure("unable to call " \
                "won, lost or finished on Hangman object",
                help=f"Got the exception {e}")

    for expected, actual in [(False, finished), (False, won), (False, lost)]:
        if expected != actual:
            # TODO add problematic method name to this error
            raise check50.Mismatch(str(expected), str(actual))

@check50.check(empty_game)
def win_games():
    """it is possible to win a game given enough guesses (26)"""
    for _ in range(5):
        play_game(win=True)

@check50.check(empty_game)
def lose_games():
    """it is possible to lose a game (returns False) given only 5 guesses"""
    for _ in range(5):
        play_game(win=False)

@check50.check(load_hangman)
def wrong_hangman():
    """creating a hangman game with incorrect parameters raises an exception"""
    params = [(-2, 3), (27, 5), (5, 0), (5, -1)]
    messages = ["-2 letter word, which does not exist",
                "27 letter word, which does not exist",
                "game with 0 guesses, which is too few",
                "game with -1 guesses, which is too few"]

    for par_pair, message in zip(params, messages):
        game = None
        try:
            game = Hangman(*par_pair)
        except Exception as e:
            pass

        if game is not None:
            raise check50.Failure("created a Hangman object for a " + message)

@check50.check(wrong_hangman)
def wrong_guesses():
    """calling hangman.guess() with an incorrect parameter raises an exception"""
    sys.path.append(os.getcwd())
    import hangman
    Hangman = hangman.Hangman
    game = Hangman(4, 5)

    inputs = ["blaat", " ", "6", 25, True, False, None]
    for wrong_input in inputs:
        accepted = True
        try:
            game.guess(wrong_input)
        except Exception:
            accepted = False

        if accepted:
            raise check50.Failure(f"guess of \"{str(wrong_input)}\" was accepted, " \
                    "but any input other than a single letter should give an " \
                    "exception")

    game.guess('A')
    accepted = True
    try:
        game.guess('A')
    except Exception:
        accepted = False

    if accepted:
        raise check50.Failure("Guessing an already guessed letter should give " \
                "an exception.")


def play_game(win):
    """Win a game (given enough guesses)."""
    sys.path.append(os.getcwd())
    import hangman
    Hangman = hangman.Hangman
    if win:
        game = Hangman(5, 26)
    else:
        game = Hangman(12, 5)
    
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    guesses = []
    num_wrong_guesses = 0

    for letter in alphabet:
        guesses.append(letter)
        correct = game.guess(letter)
        if not correct:
            num_wrong_guesses += 1

        if not letter in game.guessed_string():
            error = "A guessed letter does not appear in the game's guessed_string."
            help = f'I guessed "{letter}" but afterwards the guessed string is ' \
                   f'{game.guessed_string()}.'
            raise check50.Failure(error, help=help)

        if correct != (letter in game.pattern().lower()):
            error = "The return value of game.guess(letter) should be True if " \
                    "the guess was correct, and False otherwise."
            help = f'Got the return value {correct}.'
            raise check50.Failure(error, help=help)

        if not all(x in guesses for x in game.pattern().lower() if x != "_"):
            error = "The game pattern contains characters other than guessed " \
                    "letters and underscores."
            help = f"I found pattern {game.pattern()} with guesses " \
                   f"{''.join(guesses)}."
            raise check50.Failure(error, help=help)
        
        if game.finished():
            break
        
        if not win and num_wrong_guesses >= 5:
            error = "The game is not finished, but I should have run out of " \
                    "guesses."
            help = "I started a game with 5 guesses, and after 5 wrong guesses " \
                   "I am still playing."
            raise check50.Failure(error, help=help)
    else:
        error = "The game is not finished, but I guessed every letter in the " \
                "alphabet."
        help = "Did you implement game.finished() correctly?"
        raise check50.Failure(error, help=help)
    
    if win: 
        if game.won() != True:
            error = "I did not win the game, even while guessing all 26 letters " \
                    "in the alphabet."
            help = "Did you implement game.won() correctly?"
            raise check50.Failure(error, help=help)

        if game.lost() != False:
            error = "I lost the game, even while guessing all 26 letters."
            help = "Did you implement game.lost() correctly?"
            raise check50.Failure(error, help=help)

        if "_" in game.pattern():
            error = "Blanks in pattern after victorious game."
            help = f"Expected a full word, but the pattern is {game.pattern()}."
            raise check50.Failure(error, help=help)

    else:
        if game.won() != False:
            error = "Won the game with 5 random guesses for a " \
                    "12-letter word."
            help = "Did you implement game.won() correctly?"
            raise check50.Failure(error, help=help)

        if game.lost() != True:
            error = "Did not lose the game with 5 random guesses for a " \
                    "12-letter word."
            help = "Did you implement game.lost() correctly?"
            raise check50.Failure(error, help=help)

        if not "_" in game.pattern():
            error = "The game's pattern is filled in, even though I lost."
            help = f"Got pattern {game.pattern()}, expected a pattern with "\
                    "underscores."
            raise check50.Failure(error, help=help)
