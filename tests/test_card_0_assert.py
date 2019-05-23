from src.card import Card


def test_repr():
    ace_of_spades = Card("A", "♠")
    assert repr(ace_of_spades) == "A♠"
