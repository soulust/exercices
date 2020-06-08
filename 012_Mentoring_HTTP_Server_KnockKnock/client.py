import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
QUIT = "Exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)

print(server.recv(2048).decode(FORMAT))
while True:
    message = input().encode(FORMAT)
    if message == QUIT:
        break
    server.send(message)
    reply = server.recv(2048).decode(FORMAT)
    if not reply:
        print("Server disconnected")
        break
    print(reply)
server.close()
