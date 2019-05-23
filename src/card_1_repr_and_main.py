class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    ace_of_spades = Card("Ace", "Spades")
    print(ace_of_spades.rank)
    print(ace_of_spades.suit)
    print(ace_of_spades)
