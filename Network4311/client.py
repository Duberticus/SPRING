import threading
import socket
import http.server


stuff = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = socket.gethostbyname('www.google.com')
print(ip)

