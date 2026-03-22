import socket             


HOST = "127.0.0.1"
PORT = 8989   
ADDR = (HOST, PORT)
# Define the port on which you want to connect 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     

client.connect(ADDR)   