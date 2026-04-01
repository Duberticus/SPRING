import socket

HOST = '127.0.0.1'
PORT = 8989

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    data = client.recv(1024).decode()
    print(data)

    if "Action" in data:
        move = input("> ")
        client.sendall(move.encode())
    elif "Enter your name" in data:
        name = input("> ")
        client.sendall(name.encode())