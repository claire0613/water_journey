from Player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def make_exchange_hands_decision(self) -> bool:
        decision = False
        while True:
            user_decision = input(
                "Do you want to exchange hands in this round? (Y/N): "
            )
            if user_decision != "Y" and "N":
                print("Please answer Y or N !!!")
            else:
                if user_decision == "Y":
                    decision = True
                break
        return decision

    def show_card(self, car_index):
        self.__hand.show(index=car_index)
