from socket import *
import argparse
import ipaddress


def upload(client, message):
    client.send(("UPLOAD" + message).encode())
    response = client.recv(1024)
    print(response.decode())


def download(client):
    client.send("DOWNLOAD".encode())
    response = client.recv(1024)
    print("Message currently stored in server: " + response.decode())


def getOptions():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upload", dest="upload", action="store_true", help="Upload Message Mode")
    parser.add_argument("-d", "--download", dest="download", action="store_true", help="Download Message Mode")
    parser.add_argument(dest="serverIP")
    parser.add_argument(dest="serverPort", type=int)
    parser.add_argument(dest="message", type=str, nargs="?")
    return parser.parse_args()


def validIP(address):
    try:
        ipaddress.ip_address(address)
        return True
    except:
        return False


print("\n")
sendMessage = True
options = getOptions()

serverName = options.serverIP   # '127.0.0.1'

if not validIP(serverName):
    print("Invalid IP Address Entered. Client Exiting...")
    sendMessage = False

serverPort = options.serverPort     # 13402
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(3)


# Attempts to connect to the server
if sendMessage:
    try:
        clientSocket.connect((serverName, serverPort))
    except ConnectionRefusedError:
        print("Connection refused on host " + str(serverName) + ":" + str(serverPort))
        sendMessage = False
    except timeout:
        print("Connection failed due to exceeding the 3 second timeout. "
              "This is most likely due to an incorrect IP address entered. " "Client Exiting...")
        sendMessage = False

    except Exception as exc:
        print("Exception occurred connecting to server: " + str(exc))
        sendMessage = False


# Attempts to send message to the server
if sendMessage:
    try:
        if options.upload and options.download:
            print("Cannot call both upload and download simultaneously...")
        elif options.upload:
            if options.message is not None:
                if len(options.message) <= 150:
                    upload(clientSocket, options.message)
                else:
                    print("Cannot send message larger than 150 characters. Client exiting...")
            else:
                print("Please enter a message while uploading. Client exiting...")
        elif options.download:
            if options.message is not None:
                print("Warning: Message " + "\'" + str(options.message) + "\'" +
                      " will not be uploaded to the server in download mode.")
            download(clientSocket)
        else:
            print("Invalid argument.")
    except Exception as err:
        print("Exception occurred exchanging messages with server: " + str(err))

clientSocket.close()
