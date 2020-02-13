# Networking-Project-1
First project for CS3251

To run the server:
python3 ttweet.py <PortNumber>

To run the client:
Upload Mode:
python3 ttweetcli.py -u <HostName> <PortNumber> "message"

Download Mode:
python3 ttweetcli.py -d <HostName> <PortNumber>


Protocol Description:
Note: The client and server connect using IPv4 addressing, and the TCP protocol. 

Upload:
1. The client initiates a connection with the server. 
2. Once connected, the client sends an "UPLOAD" request followed by a message specified by the user.
3. If received properly, the server sends the response "Message Upload Successful!". On the server side, "New Message: " is printed, followed by the new message passed to the server. Otherwise an error message is sent as a response.

Download
1. The client initiates a connection with the server.
2. Once connected, the client sends a "DOWNLOAD" request to the server.
3. The server sends the currently stored message back to the client. The server will send "Empty Message" if no message is currently being stored. 


Sample Output:
0. Client - Connection refused on host hostName:portNumber
1. Client - Connection refused on host hostName:portNumber
2. Client - Connection refused on host hostName:portNumber
3. Server - Server On. Press Ctrl + C to exit.
4. Client - Message currently stored in server: Empty Message
Server - Message downloaded
5. Client - Cannot send message larger than 150 characters. Client exiting...
6. Client - Message currently stored in server: Empty Message
Server - Message downloaded
7. Client - Message Upload Successful!
Server - New Message: message1
8. Client - Message currently stored in server: message1
Server - Message downloaded
9. Client - Message Upload Successful!
Server - New Message: message 2
10. Client - Message currently stored in server: message 2
Server - Message downloaded
11. Client - Cannot send message larger than 150 characters. Client exiting...
12. Client - Message currently stored in server: message 2
Server - Message downloaded


Rules:
1. Client cannot send an empty message to the server. Outputs:
Please enter a message while uploading. Client exiting...
2. Client cannot send whitespace characters without text. Outputs:
Message must be of at least length 1 excluding whitespace characters. Client exiting...
3. Please connect the the localhost IP address 127.0.0.1
4. Please use ports between 13000 and 14000
5. There will be a timeout of 3 seconds. If the timeout is exceeded, it will output:
Connection failed due to exceeding the 3 second timeout. This is most likely due to an incorrect IP address entered. Client Exiting...
6. You cannot send a message in download mode. If a message is specified in download mode, the message will still be downloaded, but the following warning on the client side will show:
Warning: Message "message" will not be uploaded to the server in download mode.
7. If an invalid argument is specified, it will output:
Invalid Argument
8. All other exceptions will specify the exception type, or some kind of message indicating what may have gone wrong. 
