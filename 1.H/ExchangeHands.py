from Player import Player


class ExchangeHands:

    def __init__(self, exchager: Player, exchagee: Player):
        self.__exchager = exchager
        self.__exchagee = exchagee
        self.__countdown = 3

    def countdown(self):
        self.__countdown -= 1

    def exchage(self):

        self.__exchager.set_hand, self.__exchagee.set_hand = (
            self.__exchagee.set_hand,
            self.__exchager.set_hand,
        )
        print("Your hand exchanged your hand with the player:", self.__exchagee.name)
