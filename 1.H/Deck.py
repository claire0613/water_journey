from Card import Card
import random
from Player import Player


class Deck:
    def __init__(self):
        self.__cards = []

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards: list[Card]):
        self.__cards = cards

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_cards(self, player: Player) -> None:
        player.add_hand_card(self.cards.pop())
