import check50
import uva.check50.py
import check50.internal
import sys
import os
import inspect
import random
from copy import deepcopy

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

suits = ['Hearts','Diamonds','Clubs','Spades']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits_set = set(suits)
values_set = set(values)

def class_exists(module, cls):
    # check if the specified class exists
    if not hasattr(module, cls):
        raise check50.Failure(f"expected class '{cls}' to exist")


def attributes_present(cls, attributes):
    # check if each required attribute is present within the class
    for attribute in attributes:
        if not hasattr(cls, attribute):
            raise check50.Failure(f"expected class '{cls.__name__}' to have attribute '{attribute}'")


def initializer_arguments(cls, required_args):
    # get arguments for __init__
    args = inspect.getfullargspec(cls).args

    # check if the correct amount of arguments are present
    if len(required_args) != len(args):
        raise check50.Failure(f"initializer for class '{cls.__name__}' accepts {len(args)} arguments. expected {len(required_args)}")

    # check if every required argument is present
    for arg in required_args:
        if not arg in args:
            raise check50.Failure(f"expected initializer for class '{cls.__name__}' to accept argument '{arg}'")


def deck_valid(deck):
     # check if 52 different and valid cards are present
    cards = set()

    # check amount of cards
    if len(deck.cards) != 52:
        raise check50.Failure(f"found invalid amount of cards {len(deck.cards)} in deck.")

    # check each card in the deck
    for card in deck.cards:
        # check for duplicate cards
        if card.suit + card.value in cards:
            raise check50.Failure(f"found the {card.value} of {card.suit} in deck at least twice.")
        cards.add(card.suit + card.value)

        # check if the card is valid
        if not card.value in values_set or not card.suit in suits_set:
            raise check50.Failure(f"found invalid card {card.value} of {card.suit} in deck.")


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
    # check if the class exists
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Card")

    # check if the class has the required attributes
    attributes = ["suit", "value"]
    attributes_present(module.Card, attributes)


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


@check50.check(card_initializer)
def card_stringify():
    """class 'Card' can be stringified correctly."""
    module = uva.check50.py.run("cardgame.py").module

    # initialize a random card
    random_suit = random.choice(suits)
    random_value = random.choice(values)
    card = module.Card(suit=random_suit, value=random_value)

    # stringify the card and check if the value is correct
    stringified = str(card).strip()
    if stringified != f"{random_value} of {random_suit}":
        raise check50.Failure(f"unexpected message '{stringified}' with suit '{random_suit}' and value '{random_value}'. expected '{random_value} of {random_suit}'")


@check50.check(card_stringify)
def deck_initializer():
    """class 'Deck' exists, has basic attributes and can be initialized correctly."""
    # check if the class exists
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Deck")

    # check if the class has the required attributes
    attributes = ["suits", "values"]
    attributes_present(module.Deck, attributes)

    # check if __init__ accepts the correct args
    required_args = ["self"]
    initializer_arguments(module.Deck, required_args)

    # initialize a deck and check if it worked
    deck = module.Deck()
    if deck.suits != suits:
        raise check50.Failure("expected 'deck.suits' to contain all possible suits after initialization.")
    elif deck.values != values:
        raise check50.Failure("expected 'deck.values' to contain all possible values after initialization.")


@check50.check(deck_initializer)
def instantiate_cards():
    """cards are instantiated in deck."""
    module = uva.check50.py.run("cardgame.py").module

    # check if the class now has an attribute for storing cards
    attributes = ["cards"]
    attributes_present(module.Deck, attributes)

    # check if 52 different and valid cards are present
    deck_valid(module.Deck())


@check50.check(deck_initializer)
def shuffle():
    """deck changes and remains valid on shuffle()."""
    module = uva.check50.py.run("cardgame.py").module
    deck = module.Deck()

    # store original list of cards
    original_cards = [card.value + card.suit for card in deck.cards]

    # shuffle deck once, test for existance and arguments of function
    try:
        deck.shuffle()
    except NameError:
        raise check50.Failure("function 'shuffle()' does not exist within class 'Deck'.")
    except TypeError:
        raise check50.Failure("function 'shuffle()' within class 'Deck' requires arguments. expected no arguments.")

    # test if deck changed and is still valid
    new_cards = [card.value + card.suit for card in deck.cards]
    if all([original_cards[i] == new_cards[i] for i in range(len(new_cards))]):
        raise check50.Failure("deck didn't change when shuffled.")
    deck_valid(deck)


@check50.check(shuffle)
def deal():
    """deal() removes card and returns top card."""
    module = uva.check50.py.run("cardgame.py").module
    deck = module.Deck()
    deck.shuffle()

    # vars to check against
    start_len = len(deck.cards)
    last_card = deck.cards[-1]

    # deal 52 cards
    for i in range(52):
        # update vars
        start_len = len(deck.cards)
        last_card = deck.cards[-1]

        # also check existance and args
        try:
            card = deck.deal()
        except NameError:
            raise check50.Failure("function 'deal()' does not exist within class 'Deck'.")
        except TypeError:
            raise check50.Failure("function 'deal()' within class 'Deck' requires arguments. expected no arguments.")

        # check if deal decrements deck size by 1
        if len(deck.cards) != start_len - 1:
            raise check50.Failure(f"deal() changed amount of cards from {start_len} to {len(deck.cards)}. expected {start_len - 1}.")

        # check if we got the top card
        if card != last_card:
            raise check50.Failure(f"got unexpected card {card.value} of {card.suit} on deal() when top card was {last_card.value} of {last_card.suit}.")

        # check if the top card was removed
        if deck.cards[-1] != last_card:
            raise check50.Failure(f"deal() removed a card other than the top card from the deck.")