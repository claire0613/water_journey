class Showdown:
    NUM_OF_ROUNDS = 13

    def __init__(self, deck: Deck, players: list[Player]):
        self.deck = deck
        self.players = players

    def get_players(self):
        return iter(self.players)
