from socket import *
import argparse


def upload(client):
    message = input("Please enter your message...")
    client.send(("UPLOAD" + message).encode())
    response = client.recv(1024)
    print(response.decode())


def download(client):
    client.send("DOWNLOAD".encode())
    response = client.recv(1024)
    print(response.decode())


def getOptions():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upload", dest="upload", action="store_true", help="Upload Message Mode")
    parser.add_argument("-d", "--download", dest="download", action="store_true", help="Download Message Mode")
    parser.add_argument(dest="serverIP")
    parser.add_argument(dest="serverPort", type=int)
    return parser.parse_args()


options = getOptions()
print(options.upload)
print(options.download)

serverName = options.serverIP   # '127.0.0.1'
serverPort = options.serverPort     # 13402
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

if options.upload and options.download:
    print("Cannot call both upload and download simultaneously...")
elif options.upload:
    upload(clientSocket)
elif options.download:
    download(clientSocket)
else:
    print("Invalid argument.")

clientSocket.close()
