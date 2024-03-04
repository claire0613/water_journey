from abc import ABC, abstractmethod
from Hand import Hand


class Player(ABC):
    def __init__(self):
        self.__point = 0
        self.__name = ""
        self.__hand = Hand()

    @property
    def point(self):
        return self.__point

    @point.setter
    def gain_point(self, point):
        self.__point += point
        return self.__point

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def add_hand_card(self, card):
        self.__hand.add_card(card)

    @abstractmethod
    def show_card(self):
        return NotImplemented

    @abstractmethod
    def make_exchange_hands_decision(self) -> bool:
        return NotImplemented

