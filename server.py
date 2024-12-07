import socket

s = socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting for connections")


while True:
    c,addr= s.accept()
    Name= c.recv(1024).decode()
    print("connected successfully",addr,Name)
    while True:
        stext = input("Server: ")
        stext = "Server: " + stext
        c.send(bytes(stext, 'utf-8'))
        rtext = c.recv(1024).decode()
        print(rtext)
        if stext == "Server: quit" or rtext == "Client: quit":
            break

    c.send(bytes("you are a wonderful human being", 'utf-8'))
    c.close()

