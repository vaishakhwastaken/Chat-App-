import socket

c = socket.socket()
c.connect(("localhost",9999))
Name = input("Name: ")
c.send(bytes(Name,'utf-8'))
while True:
    stext = c.recv(1024).decode()
    print(stext)
    rtext = input("Client: ")
    rtext = "Client: " + rtext
    rtext = c.send(bytes(rtext, "utf-8"))
    if stext == "Server: quit" or rtext == "Client: quit":
        break
message = c.recv(1024).decode()

print(message)