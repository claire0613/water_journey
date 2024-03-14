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

    @abstractmethod
    def show_card(self):
        return NotImplemented

    @abstractmethod
    def make_exchange_hands_decision(self) -> bool:
        return NotImplemented

    @property
    def hand(self) -> Hand:
        return self.__hand

    @hand.setter
    def set_hand(self, hand: Hand):
        self.__hand = hand
    
    def take_turn(self):
        self.make_exchange_hands_decision()
        

