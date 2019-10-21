import check50
import uva.check50.py
import check50.internal
import sys
import os
import inspect
import random

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

suits = ['Hearts','Diamonds','Clubs','Spades']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def class_exists(module, cls):
    if not hasattr(module, cls):
        raise check50.Failure(f"expected class '{cls}' to exist")


def properties_present(cls, attributes):
    for attribute in attributes:
        if not hasattr(cls, attribute):
            raise check50.Failure(f"expected class '{cls.__name__}' to have property '{attribute}'")


def initializer_arguments(cls, required_args):
    args = inspect.getfullargspec(cls).args

    for arg in required_args:
        if not arg in args:
            raise check50.Failure(f"expected initializer for class '{cls.__name__}' to accept argument '{arg}'")


@check50.check()
def exists():
    """cardgame.py exists."""
    check50.exists("cardgame.py")


@check50.check(exists)
def compiles():
    """cardgame.py compiles."""
    uva.check50.py.compile("cardgame.py")
    module = uva.check50.py.run("cardgame.py").module


@check50.check(compiles)
def card_class_basic():
    """class 'Card' exists and has basic attributes."""
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Card")

    # check if the class has the required properties
    properties = ["suit", "value"]
    properties_present(module.Card, properties)


@check50.check(card_class_basic)
def card_initializer():
    """class 'Card' can be initialized correctly."""
    module = uva.check50.py.run("cardgame.py").module

    # check if __init__ accepts the correct args
    required_args = ["self", "suit", "value"]
    initializer_arguments(module.Card, required_args)

    # initialize a random card
    random_suit = random.choice(suits)
    random_value = random.choice(values)
    card = module.Card(suit=random_suit, value=random_value)

    # check if the initializer worked
    if card.suit != random_suit:
        raise check50.Failure(f"class 'Card' was initialized with unexpected suit '{card.suit}'. expected '{random_suit}'")
    elif card.value != random_value:
        raise check50.Failure(f"class 'Card' was initialized with unexpected value '{card.value}'. expected '{random_value}'")