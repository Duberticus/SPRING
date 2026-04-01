from deckClass import Deck
from treys import Card, Evaluator

class Board:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.community_cards = []
        self.current_bet = 0
        self.deck = Deck()
        self.deck.shuffle()

    def add_to_pot(self, amount):
        self.pot += amount

    def deal_hole_cards(self):
        #clear previous hand
        for p in self.players:
            p.hole_cards = []

        for _ in range(2):
            for p in self.players:
                if p.status != "out":
                    p.hole_cards.append(self.deck.deal())

    def burn(self):
        self.deck.deal()#discard top card

    def deal_flop(self):
        self.burn()
        self.community_cards.extend([self.deck.deal() for _ in range(3)])
        return self.community_cards

    def deal_turn(self):
        self.burn()
        self.community_cards.append(self.deck.deal())
        return self.community_cards

    def deal_river(self):
        self.burn()
        self.community_cards.append(self.deck.deal())
        return self.community_cards

    def reset_bets(self):
        self.current_bet = 0
        for p in self.players:
            p.current_bet = 0

    def handle_action(self, player, action, amount=None):
        if player.status != "active":
            raise ValueError(f"{player.name} cannot act")

        if action == "fold":
            player.fold()
            return f"{player.name} folds"

        elif action == "call":
            to_call = self.current_bet - player.current_bet
            bet = player.call(to_call)
            self.add_to_pot(bet)
            return f"{player.name} calls {bet}"

        elif action == "raise":
            if amount is None:
                raise ValueError("Raise requires amount")

            if amount < self.current_bet:
                raise ValueError("Must raise above current bet")

            to_add = amount - player.current_bet
            bet = player.bet(to_add)

            self.current_bet = amount
            self.add_to_pot(bet)

            return f"{player.name} raises to {amount}"

        elif action == "check":
            if player.current_bet != self.current_bet:
                raise ValueError("Cannot check")
            player.check()
            return f"{player.name} checks"

        else:
            raise ValueError("Invalid action")

    def evaluate_winner(self):
        evaluator = Evaluator()
        board = [Card.new(c) for c in self.community_cards]

        best_score = float('inf')
        winner = None

        for p in self.players:
            if p.status == "folded":
                continue

            hand = [Card.new(c) for c in p.hole_cards]
            score = evaluator.evaluate(board, hand)

            if score < best_score:
                best_score = score
                winner = p

        return winner

    def award_pot(self, winner):
        winner.chips += self.pot
        print(f"{winner.name} wins {self.pot} chips!")
        self.pot = 0
