import socket             

# Create a socket object 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         

# Define the port on which you want to connect 
port = 8989              

# connect to the server on local computer 
sock.connect(('127.0.0.1', port)) 

# receive data from the server and decoding to get the string.
msg = sock.recv(1024).decode()
# close the connection 

sock.close()

#sock.connect(('127.0.0.1', port)) 
#sock.send()

print(msg)