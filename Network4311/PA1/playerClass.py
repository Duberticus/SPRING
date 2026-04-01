class Player:
    def __init__(self, name, chips=5000):
        self.name = name
        self.chips = chips
        self.hole_cards = []
        self.current_bet = 0
        self.status = "active"

    def bet(self, amount):
        if self.status != "active":
            raise ValueError(f"{self.name} cannot bet when {self.status}")

        if amount > self.chips:
            raise ValueError(f"{self.name} only has {self.chips} chips")

        self.chips -= amount
        self.current_bet += amount

        if self.chips == 0:
            self.status = "all_in"

        return amount

    def call(self, amount):
        if self.status != "active":
            raise ValueError(f"{self.name} cannot call")

        amount = min(amount, self.chips)
        self.chips -= amount
        self.current_bet += amount

        if self.chips == 0:
            self.status = "all_in"

        return amount

    def fold(self):
        self.status = "folded"

    def check(self):
        if self.status != "active":
            raise ValueError(f"{self.name} cannot check")

    def reset(self):
        self.current_bet = 0
        self.hole_cards = []
        if self.chips == 0:
            self.status = "out"
        elif self.status != "folded":
            self.status = "active"

    def __str__(self):
        return f"{self.name} ({self.chips} chips, {self.status})"


if __name__ == "__main__":
    #test
    me = Player("Alice")
    print(me.name, me.chips, me.status)
    me.bet(100)
    print(me.name, me.chips, me.current_bet, me.status)
    me.call(200)
    print(me.name, me.chips, me.current_bet, me.status)
