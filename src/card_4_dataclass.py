from dataclasses import dataclass
from random import choice


@dataclass
class Card:
    """A playing card. Can be added and converted to int based on rank."""
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("♣", "♦", "♥", "♠")
    RANK_VALUES = {"A": 1, "J": 10, "Q": 10, "K": 10}
    SUIT_SYMBOLS = {"Club": "♣", "Diamond": "♦", "Heart": "♥", "Spade": "♠"}
    rank: str
    suit: str

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
    print(Card.random())
