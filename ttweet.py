from socket import *

serverMessage = "Empty Message"
serverPort = 13402
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server On. Press Ctrl + C to exit.')
while True:
    connectionSocket, addr = serverSocket.accept()

    message = connectionSocket.recv(1024).decode()
    response = ""
    if message[0:6] == "UPLOAD":
        serverMessage = message[6::]
        response = "Message Uploaded Successfully"
        print("New Message: ", serverMessage)
    elif message[0:8] == "DOWNLOAD":
        response = serverMessage
        print("Message downloaded")
    else:
        print("Error processing request")

    connectionSocket.send(response.encode())
    connectionSocket.close()
