from socket import *

serverPort = 25565
serverPortStr = '25565'
serverPort2 = 25569
serverPort2Str = '25569'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket2 = socket(AF_INET, SOCK_STREAM)
serverSocket2.bind(('192.168.1.7', serverPort2))
serverSocket.bind(('192.168.1.7', serverPort))
serverSocket.listen(1)
serverSocket2.listen(2)
print('The server is ready to connect to using ports: ' + serverPortStr + " and " + serverPort2Str)
connectionSocket, addr = serverSocket.accept()
connectionSocket2, addr = serverSocket2.accept()

while True:
    sentence = (connectionSocket.recv(1024).decode())
    print("Client 1: " + sentence)
    if(sentence != ''):
        connectionSocket2.send(sentence.encode())
    else:
        break
    sentence2 = (connectionSocket2.recv(1024).decode())
    print("Client 2: " + sentence2)
    if(sentence2 != 'no'):
        connectionSocket.send(sentence2.encode())
    else:
        break