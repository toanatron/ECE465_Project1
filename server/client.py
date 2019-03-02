# This program is used as a client connecting to a server using TCP and sends HTTP requests
# Run this program by using this command: python client.py <server name> <server port number> <file name>
# Authors: Vincent Guevara, Tianhui Xu, Toan Tran

import sys
import socket
import select, string


def main():
    #
    #  Handle command line arguments
    # example: client.py "mason.gmu.edu" 1100 "/index.html"
    if len(sys.argv) == 4:
        serverName = sys.argv[1]
        serverPort = int(sys.argv[2])
        fileName = sys.argv[3]

    else:
        print 'Usage:     TCPClient <server name> <server port number> <filename>' #example: client.py "mason.gmu.edu" 1100 "/index.html"
        return
    #creates socket connection
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect((serverName, serverPort))
    except:
        print('Unable to connect to server')
        sys.exit()
    #send HTTP request to server
    request = 'GET '+fileName+' HTTP/1.1'
    clientSocket.send(request)
    #print out data sent from server
    try:
        reply = clientSocket.recv(4098)
        reply2 = clientSocket.recv(4098)
        print(reply)
        print(reply2)
    except:
        print('file was not found')



if __name__ == '__main__':
    main()
