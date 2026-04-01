import socket
from playerClass import Player
from boardClass import Board

HOST = '127.0.0.1'
PORT = 8989

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

connections = []
players = []


print("Server started. Waiting for 2 players")

# ===== CONNECT PLAYERS =====
while len(connections) < 2:

    conn, addr = server.accept()
    print("Connected:", addr)

    conn.sendall("Enter your name: ".encode())
    name = conn.recv(1024).decode().strip()

    player = Player(name)
    players.append(player)
    connections.append(conn)

    conn.sendall(f"Welcome {name}!\n".encode())

# ===== CREATE GAME =====
board = Board(players)
board.deal_hole_cards()

def send_to(conn, msg):
    conn.sendall((msg + "\n").encode())

def broadcast(msg):
    for c in connections:
        send_to(c, msg)

# ===== BETTING ROUND =====
def betting_round():
    for i, player in enumerate(players):
        if player.status != "active":
            continue

        conn = connections[i]

        while True:
            try:
                send_to(conn, f"Your hand: {player.hole_cards}")
                send_to(conn, f"Pot: {board.pot}")
                send_to(conn, f"Current bet: {board.current_bet}")
                send_to(conn, "Action (fold/call/check/raise X):")

                data = conn.recv(1024).decode().strip().lower()

                if data in ["fold", "call", "check"]:
                    result = board.handle_action(player, data)

                elif data.startswith("raise"):
                    amount = int(data.split()[1])
                    result = board.handle_action(player, "raise", amount)

                else:
                    send_to(conn, "Invalid input.")
                    continue

                # Broadcast action result to all clients
                broadcast(result)

                # Broadcast shared game state after action
                broadcast(f"Pot: {board.pot}")
                broadcast(f"Current bet: {board.current_bet}")
                for p in players:
                    broadcast(f"{p.name}: chips={p.chips}, current_bet={p.current_bet}, status={p.status}")

                break

            except Exception as e:
                send_to(conn, f"Error: {e}")

# ===== GAME FLOW =====
broadcast("Starting game...")
betting_round()

broadcast("Flop:")
broadcast(str(board.deal_flop()))
board.reset_bets()
betting_round()

broadcast("Turn:")
broadcast(str(board.deal_turn()))
board.reset_bets()
betting_round()

broadcast("River:")
broadcast(str(board.deal_river()))
board.reset_bets()
betting_round()

winner = board.evaluate_winner()
board.award_pot(winner)

broadcast(f"Winner is {winner.name}")

# Close connections
for i in range(100):
    conn.sendall(f"imma blow up your terminal {i}\n".encode())

for c in connections:
    c.close()