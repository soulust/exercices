import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
QUIT = "Exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(1)

while True:
    print(f"[LISTENING] Server is listening on {SERVER}")
    client, address = server.accept()
    print(f"[NEW CONECTION] {address} connected.")
    client.send("Knock, knock !".encode(FORMAT))
    
    while True:
        message = client.recv(2048).decode(FORMAT)
        if message == QUIT:
            client.close()
            break
        elif message == "Who's there ?":
            print(message)
            client.send("Amarillo".encode(FORMAT))
        elif message == "Amarillo who ?":
            print(message)
            client.send("Amarillo, nice guy !".encode(FORMAT))
            print("The joke is over, bye !")
            client.close()
            break
        else:
            client.send("Get back to the joke \nKnock, knock !".encode(FORMAT))
            #client.send(input().encode(FORMAT))

