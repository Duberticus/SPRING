import threading
import socket


HOST = "127.0.0.1"
PORT = 8989
ADDR = (HOST, PORT)
#TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)



def client_handler(conn,address):
    print(f"{address} connected")

    connected = True
    while connected:
        msg = conn.recv(1024).decode('utf-8')
        #conn.settimeout(10)
        print('hello')


def start():
    server.listen()
    while True:
        conn,address = server.accept()
        thread = threading.Thread(target =client_handler,args = (conn,address))
        thread.start()
        print(threading.active_count() -1 )
        #print('benchode')    
    
print("starting")

start()