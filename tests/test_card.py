import dataclasses
from random import seed

import pytest

from src.card import Card


def test_init_symbol():
    card = Card("2", "♠")
    assert isinstance(card, Card)


def test_init_name():
    card = Card("2", "Spade")
    assert isinstance(card, Card)


def test_init_name_plural():
    card = Card("2", "Spades")
    assert isinstance(card, Card)


def test_init_random():
    seed(12)
    card = Card.random()
    print(card)
    assert isinstance(card, Card)


def test_init_random_multiple():
    """Test for random outputting multiple values. Requires hash."""
    cards = {Card.random() for _ in range(100)}
    assert len(cards) > 1  # This has a (1/52)**100 chance of randomly failing
    seed(1)
    card_1 = Card.random()
    seed(2)
    card_2 = Card.random()
    assert card_1 != card_2


@pytest.fixture
def two_of_spades():
    return Card("2", "♠")


@pytest.fixture
def five_of_hearts():
    return Card("5", "♥")


@pytest.fixture
def king_of_diamonds():
    return Card("K", "♦")


@pytest.fixture
def deck():
    return [
        Card("5", "♥"),
        Card("7", "♠"),
        Card("2", "♣"),
        Card("A", "♠"),
        Card("A", "♦"),
    ]


def test_str(two_of_spades, five_of_hearts):
    assert str(two_of_spades) == "2♠"
    assert str(five_of_hearts) == "5♥"


def test_repr(deck):
    assert repr(deck) == "[5♥, 7♠, 2♣, A♠, A♦]"


def test_eq(two_of_spades, five_of_hearts):
    assert two_of_spades == two_of_spades
    assert two_of_spades == Card("2", "♠")
    assert two_of_spades != five_of_hearts


def test_add(two_of_spades, king_of_diamonds):
    assert two_of_spades + two_of_spades == 4
    assert two_of_spades + 2 == 4
    assert 2 + two_of_spades == 4
    assert king_of_diamonds + two_of_spades == 12
    assert king_of_diamonds + 1 == 11


def test_sum(deck):
    assert sum(deck) == 16


def test_ordering(two_of_spades, five_of_hearts, deck):
    assert two_of_spades < five_of_hearts
    assert five_of_hearts > two_of_spades
    assert str(sorted(deck)) == "[A♦, A♠, 2♣, 5♥, 7♠]"


def test_hash(two_of_spades):
    hash(two_of_spades)


def test_frozen(two_of_spades):
    with pytest.raises(dataclasses.FrozenInstanceError):
        two_of_spades.rank = "14"
    with pytest.raises(dataclasses.FrozenInstanceError):
        two_of_spades.suit = "B"


def test_validation():
    with pytest.raises(ValueError):
        Card("52", "♣")
    with pytest.raises(ValueError):
        Card("2", "B")


def test_all():
    assert Card.all().__next__() == Card("A", "♣")
    assert len(list(Card.all())) == len(Card.SUITS) * len(Card.RANKS)
