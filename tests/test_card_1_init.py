from src.card import Card


def test_init_symbol():
    card = Card("2", "♠")
    assert isinstance(card, Card)


def test_repr():
    ace_of_spades = Card("A", "♠")
    assert repr(ace_of_spades) == "A♠"
