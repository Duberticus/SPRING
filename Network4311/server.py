import threading
import socket

HOST = "127.0.0.1"
PORT = 8989

#TCP connection
SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

SS.bind((HOST, PORT))

SS.listen()

#print(connection)

#s.connect((host_ip,PORT)) 

def listen():
    return

