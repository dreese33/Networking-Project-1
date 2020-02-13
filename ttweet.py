from socket import *
import argparse


startServer = True

try:
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="serverPort", type=int)
    options = parser.parse_args()

    serverMessage = "Empty Message"
    serverPort = options.serverPort      # 13402
    serverSocket = socket(AF_INET, SOCK_STREAM)
except Exception as err:
    startServer = False
    print("The following exception occurred: " + str(err))

try:
    serverSocket.bind(('', serverPort))
except Exception as err:
    startServer = False
    print("Error binding to port " + str(serverPort) + ". Error: " + str(err))

if startServer:
    serverSocket.listen(1)
    print('Server On. Press Ctrl + C to exit.')
    while True:
        try:
            connectionSocket, addr = serverSocket.accept()

            message = connectionSocket.recv(1024).decode()
            response = ""
            if message[0:6] == "UPLOAD":
                serverMessage = message[6::]
                response = "Message Upload Successful!"
                print("New Message: " + "\"" + serverMessage + "\"")
            elif message[0:8] == "DOWNLOAD":
                response = serverMessage
                print("Message downloaded")
            else:
                print("Error processing request")

            connectionSocket.send(response.encode())
        except Exception as err:
            try:
                connectionSocket.send(("Error processing request: " + str(err)).encode())
            except Exception as exc:
                print("Something went wrong sending message back to client: " + str(exc))
        connectionSocket.close()

