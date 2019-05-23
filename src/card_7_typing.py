from __future__ import annotations

from dataclasses import dataclass, field
from random import choice
from typing import Union


@dataclass(order=True)
class Card:
    """A playing card. Can be added and converted to int based on rank. Ordered."""
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("♣", "♦", "♥", "♠")
    RANK_VALUES = {"A": 1, "J": 10, "Q": 10, "K": 10}
    SUIT_SYMBOLS = {"Club": "♣", "Diamond": "♦", "Heart": "♥", "Spade": "♠"}
    sort_index: int = field(init=False, repr=False)  # This must come first for sorting.
    rank: str
    suit: str

    def _add_sort_index_field(self) -> None:
        """Add field `sort_index` for card order and verifies valid rank and suit."""
        try:
            rank_i = self.RANKS.index(self.rank)
        except ValueError:
            print(f"Card rank ({self.rank}) not in {self.RANKS}\n")
            raise
        try:
            suit_i = self.SUITS.index(self.suit)
        except ValueError:
            print(f"Card suit ({self.suit}) not in {self.SUITS}")
            raise
        self.sort_index = rank_i * len(self.SUITS) + suit_i

    def __post_init__(self) -> None:
        self._add_sort_index_field()

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __int__(self) -> int:
        if self.rank in self.RANK_VALUES:
            return self.RANK_VALUES[self.rank]
        else:
            return int(self.rank)

    def __add__(self, other: Union[Card, int]) -> int:
        return int(self) + int(other)

    def __radd__(self, other: Union[Card, int]) -> int:
        return self.__add__(other)

    @classmethod
    def random(cls) -> Card:
        """Return a random playing card from available ranks and suits."""
        return cls(choice(cls.RANKS), choice(cls.SUITS))


if __name__ == "__main__":
    ace_of_spades = Card("A", "♠")
    print(ace_of_spades)
    deck = [Card.random() for _ in range(10)]
    print(deck)
    print(sorted(deck))
