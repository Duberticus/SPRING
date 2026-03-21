import threading
import socket

def TakeInput(var):
    if var == 1:
        print("making new user")
    if var == 2:
        print("making ")
    return



HOST = "127.0.0.1"
PORT = 8989

#TCP connection
SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
SS.bind((HOST, PORT))
SS.listen()

while True:
    client,address = SS.accept()
    print ('Got connection from client', address )
    client.send('Enter an alias'.encode()) #client side
    client.close()