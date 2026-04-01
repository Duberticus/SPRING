import random

class Deck:
    def __init__(self, deckPath='B:/SPRING/Network4311/PA1/deck.csv'):
        self.cards = self._create_deck(deckPath)

    def _create_deck(self, deckPath):
        deck = []
        with open(deckPath, encoding='utf-8', mode='r') as d:
            for card in d:
                deck.append(card.strip())
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()