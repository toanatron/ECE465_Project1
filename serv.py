from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
while 1:
    sentence = connectionSocket.recv(1024)
    print(sentence.decode("utf-8"))
    c = sentence.decode("utf-8")
    if c == "exit" or c == "EXIT":  # if client sends exit in his text we will stop the server
        print("Server will not close")
        break
connectionSocket.close()