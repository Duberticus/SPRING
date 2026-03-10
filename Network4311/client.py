import threading
import socket
import http.server


stuff = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

stuff.connect(("127.0.0.1", 8989))
stuff.send(b"hello")
stuff.close()


