from dataclasses import dataclass, field
from random import choice, shuffle


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

    def _add_sort_index_field(self):
        """Add field `sort_index` for card order."""
        rank_i = self.RANKS.index(self.rank)
        suit_i = self.SUITS.index(self.suit)
        self.sort_index = rank_i * len(self.SUITS) + suit_i

    def __post_init__(self):
        self._add_sort_index_field()

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __int__(self):
        if self.rank in self.RANK_VALUES:
            return self.RANK_VALUES[self.rank]
        else:
            return int(self.rank)

    def __add__(self, other):
        return int(self) + int(other)

    def __radd__(self, other):
        return self.__add__(other)

    @classmethod
    def random(cls):
        """Return a random playing card from available ranks and suits."""
        return cls(choice(cls.RANKS), choice(cls.SUITS))


if __name__ == "__main__":
    ace_of_spades = Card("A", "♠")
    print(ace_of_spades)
    hand = [Card.random() for _ in range(10)]
    print(hand)
    print(sorted(hand))
    shuffle(hand)
    print(hand)
