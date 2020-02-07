from socket import *

def upload(client):
    message = input("Please enter your message...")
    client.send(("UPLOAD" + message).encode())
    response = client.recv(1024)
    print(response.decode())


def download(client):
    client.send("DOWNLOAD".encode())
    response = client.recv(1024)
    print(response.decode())


serverName = '127.0.0.1'
serverPort = 13402
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
upload(clientSocket)
clientSocket.close()
