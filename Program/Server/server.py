from socket import *

# Initializes Client Ports to be connected to.
serverPort = 25565
serverPortStr = '25565'
serverPort2 = 25569
serverPort2Str = '25569'

# Initializes Sockets for both Clients.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket2 = socket(AF_INET, SOCK_STREAM)

# Binds Sockets to ip's and ports needed for the server to
# Communicate Properly.
serverSocket2.bind(('192.168.1.7', serverPort2))
serverSocket.bind(('192.168.1.7', serverPort))
serverSocket.listen(1)
serverSocket2.listen(2)

# Shows server is ready to be connected to.
print('The server is ready to connect to using ports: ' + serverPortStr + " and " + serverPort2Str)

# Accepts connection so that actual game can be started.
connectionSocket, addr = serverSocket.accept()
print("Client 1 Connected.")
connectionSocket2, addr = serverSocket2.accept()
print("Client 2 Connected")

# Infinite loop that allows transmissions to be received and sent
# unless the clients close the connections.
while True:

    # Creates String that receives code from first client.
    sentence = (connectionSocket.recv(1024).decode())
    print("Client 1: " + sentence)

    # If sentence is equal to blank space then it sends the
    # transmission to the other client.
    if(sentence != ''):
        connectionSocket2.send(sentence.encode())
    else:
        break

    # Creates second variable to hold second clients transmission
    # and sends it to the first client.
    sentence2 = (connectionSocket2.recv(1024).decode())
    print("Client 2: " + sentence2)

    # If the second second is equal to no, it kills the program to exit.
    if(sentence2 != 'no'):
        connectionSocket.send(sentence2.encode())
    else:
        break
