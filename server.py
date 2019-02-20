import socket
import threading

def server_mode():
    host= """----------enter the server ip here-------------"""
    port = 6666
    s = socket.socket()
    s.bind((host, port))
    s.listen(2)

    c, address = s.accept()
    nick1 =  c.recv(1024)
    print("Connection from: ", str(address),"nickname->",nick1.decode())
    c2, address2 = s.accept()
    nick2 = c2.recv(1024)
    print("Connection 2 from ", str(address2), "nickname->",nick2.decode())
    c.send(nick2)
    c2.send(nick1)

    def recieve1():
        data = c.recv(1024)
        c2.send(data)
        data = ""

    def recieve2():
        data2 = c2.recv(1024)
        c.send(data2)
        data2 = ""

    while True:

        th2 = threading.Thread(target=recieve2)
        th = threading.Thread(target=recieve1)
        th.start()
        
    c.close()

def client_mode():
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
            #data = s.recv(1024)
            print(str(nick2.decode()),":", data.decode())
            data = ""

    while True:

        t1 = threading.Thread(target=recieve)
        t1.start()
        message = str(input())
        encode_message = message.encode()
        s.send(encode_message)
    s.close()

def otonom_mode():
    host= """----------enter the server ip here-------------"""
    port = 6666

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    c, address = s.accept()
    print("Connection from: ", str(address))

    encode_sip = host.encode()
    while True:
        data = c.recv(1024)
        if not data:
            break
        decode_data = data.decode()
        if str(decode_data) == "whatsurip":
            c.send(encode_sip)
        if str(decode_data) == "whatsmyip":
            c.send(address.encode())
        else:
            invalidc = "invalide command"
        c.send(invalidc.encode())
    c.close()


print("Please choose the mod\n1 Server mode\n2 Client mode\n3 Otonom mode")
choice = str(input())

if choice == "1":
    server_mode()
elif choice == "2":
    client_mode()
elif chocie == "3":
    otonom_mode()

