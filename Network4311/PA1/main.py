from playerClass import Player
from boardClass import Board
from deckClass import Deck




# def test_board():
#     p1 = Player("Alice")
#     p2 = Player("Bob")

#     board = Board([p1, p2])

#     deck = Deck()

#     print("\n--- Betting Round ---")
#     toputin = int(input('Alice how much are you putting in?'))
#     board.place_bet(p1, toputin)
#     toputin2 = int(input('Bob how much are you raising?'))
#     board.place_bet(p2, toputin2)
#     #tp = board.deal_hole_cards(deck)

#     print("Pot:", board.pot)


#     print()
#     print("\n--- Player States ---")
#     for p in board.players:
#         print(p.name, p.chips, p.current_bet, p.status)
       # print(tp)
    
    
# def testDeck():   
#     deck = Deck()
#     deck.shuffle()

#     print("Top 5 cards:")
#     for _ in range(5):
#         print(deck.deal())





# def testGame():
#     p1 = Player("Terry")
#     p2 = Player("Jerry")
#     p3 = Player('Alfonso')
#     p4 = Player('Harry')

#     board = Board([p1, p2, p3, p4])

#     print("\n--- Deal hole cards ---")
#     board.deal_hole_cards()
#     for p in board.players:
#         print(p.name, "hole cards:", p.hole_cards)

#     print("\n--- Buy In ---")
#     for p in board.players:
#         toputin = int(input(f"{p.name} how much are you putting in? "))
#         board.place_bet(p, toputin)

#     print("--- Player States ---")
#     for p in board.players:
#         print(p.name, p.chips, p.current_bet, p.status, p.hole_cards)

#     print("--- Flop ---")
#     flop = board.deal_flop()
#     print("Flop community cards:", flop)######    Flop


   
   
   
   
#     print("\n--- Round 2 ---")########Turn

#     for p in board.players:
#         toputin = int(input(f"{p.name} how much are you putting in for the turn? "))
#         board.place_bet(p, toputin)

#     print("--- Player States ---")
#     for p in board.players:
#         print(p.name, p.chips, p.current_bet, p.status,p.hole_cards)

#     print("--- River ---")  
#     turn = board.deal_turn()
#     print("turn community cards:", turn) ################ Turn  



   
   
   
#     print("\n--- Round 3 ---")  ################ RIVER

#     for p in board.players:
#         toputin = int(input(f"{p.name} how much are you putting in for the River? "))
#         board.place_bet(p, toputin)

#     print("--- Player States ---")
#     for p in board.players:
#         print(p.name, p.chips, p.current_bet, p.status, p.hole_cards)

#     print("--- River ---") 
#     river = board.deal_river()
#     print("River community cards:", river)  ################ RIVER

#     winner = board.evaluate_winner()
#     print("Winner:", winner)
   
def playGame():
    
    p1 = Player("Terry")
    p2 = Player("Jerry")
    p3 = Player("Alfonso")
    p4 = Player("Harry")
    

    board = Board([p1,p2,p3,p4])

    print("\n--- Deal Hole Cards ---")
    board.deal_hole_cards()
    for p in board.players:
        print(p.name, p.hole_cards)

    ######## PRE-FLOP
    print("\n--- Pre-Flop Betting ---")
    betting_round(board)

    ####### FLOP
    print("\n--- Flop ---")
    print(board.deal_flop())

    board.reset_bets()
    betting_round(board)

    ###### TURN
    print("\n--- Turn ---")
    print(board.deal_turn())

    board.reset_bets()
    betting_round(board)

    ############ RIVER
    print("\n--- River ---")
    print(board.deal_river())

    board.reset_bets()
    betting_round(board)

    # ===== WINNER =====
    winner = board.evaluate_winner()
    board.award_pot(winner)

######## takes input will be used by socket later
def get_action_input(player):
    while True:
        try:
            raw = input(f"{player.name} action (fold/call/check/raise X): ").strip().lower()

            if raw in ["fold", "call", "check"]:
                return raw, None

            elif raw.startswith("raise"):
                amount = int(raw.split()[1])
                return "raise", amount

            else:
                print("Invalid input.")

        except:
            print("Invalid input.")


def betting_round(board):
    for p in board.players:
        if p.status != "active":
            continue

        while True:
            action, amount = get_action_input(p)
            try:
                result = board.handle_action(p, action, amount)
                print(result)
                break
            except Exception as e:
                print("Error:", e)



if __name__ == "__main__":
    #test_board()
    #testDeck()
    #testGame()
    playGame()