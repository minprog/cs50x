import check50
import uva.check50.py
import check50.internal

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

def class_exists(module, cls):
    if not hasattr(module, cls):
        raise check50.Failure(f"expected class {{cls}} to exist")


def properties_present(cls, attributes):
    for attribute in attributes:
        if not hasattr(cls, attribute):
            raise check50.Failure(f"expected class {{cls.__name__}} to have property {{attribute}}")


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
def card_class_basic(stdout):
    """class Card exists and has basic attributes."""
    module = uva.check50.py.run("cardgame.py").module
    class_exists(module, "Card")

    properties = ["suit", "value"]
    properties_present(module.Card, properties)