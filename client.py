import socket
import threading
host = input("Enter the ip-> ")
port = int(input("Enter the port number-> "))
nick = str(input("Enter your nickname-> ")).encode()

s = socket.socket()
s.connect((host, port))
s.send(nick)
nick2 = s.recv(1024)

message = "a"

def recieve():
    data = s.recv(1024)
    while data != "":
        print(str(nick2.decode()),":", data.decode())
        data = ""

while True:

    t1 = threading.Thread(target=recieve)
    t1.start()
    message = str(input())
    encode_message = message.encode()
    s.send(encode_message)

s.close()
~                           
