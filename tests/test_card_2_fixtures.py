import pytest

from src.card import Card


def test_init_symbol():
    card = Card("2", "♠")
    assert isinstance(card, Card)


@pytest.fixture
def two_of_spades():
    return Card("2", "♠")


def test_repr(two_of_spades):
    assert repr(two_of_spades) == "2♠"
