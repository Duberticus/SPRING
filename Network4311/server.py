import threading
import socket

HOST = "127.0.0.1"
PORT = 8989

#TCP connection
SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

SS.bind((HOST, PORT))

SS.listen()
print("hello")
#print(connection)

#s.connect((host_ip,PORT)) 


def listen():
    print("Listening")
    while True:
        connection, address = SS.accept()
        print(f"Connected by {address}")
        data = connection.recv(1024)
        print(f"Received: {data.decode()}")
        connection.close()

listen()


