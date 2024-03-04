from enum import Enum


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.__rank = rank
        self.__suit = suit

    @property
    def rank(self):
        """get rank"""

        return self.__rank

    @property
    def suit(self):
        """get suit"""
        return self.__suit

    def __repr__(self):
        return f"Card(Rank={self.__rank.name}, Suit={self.__suit.name})"

    @classmethod
    def compare_cards(cls, card1: "Card", card2: "Card"):
        """
        比較兩張卡的大小
        如果 card1 > card2, return 1
        如果 card2 < card1, return -1
        如果 card1 == card2, return 0

        """
        # 先比較rank
        if card1.__rank.value > card2.__rank.value:
            return 1
        elif card1.__rank.value < card2.__rank.value:
            return -1
        else:
            if card1.__suit.value > card2.__suit.value:
                return 1
            elif card1.__suit.value < card2.__suit.value:
                return -1

            return 0
