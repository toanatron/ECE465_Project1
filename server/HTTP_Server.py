# This program is used to create a multithreaded server that can display a webpage
# Run this program first before the client and connecting to server from browser
# To run the program use this command: python HTTP_Server.py <port number>
# Authors: Vincent Guevara, Tianhui Xu, Toan Tran

#import socket module
import socket
# In order to terminate the program
import sys

#import thread module
import thread

#thread creation routine
def clientthread(conn):
    while True:
        try:
            #client request file
            message = conn.recv(2048)
            if not message:
                break
            #read in file requested
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            #send the OK file was found to client
            conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            #send all information of file
            conn.sendall(outputdata)
            conn.send('\r\n')
            conn.close()
        except IOError:
            conn.close()
            break
    sys.exit()

def main():
    #Prepare a sever socket allowing for reusing of address
    serverPort = int(sys.argv[1])
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        serverSocket.bind(('', serverPort))
    except socket.error:
        print("binding failed")
        sys.exit()
    serverSocket.listen(10)
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
        print("Connected with "+ addr[0]+":"+str(addr[1]))
        #create a new thread
        thread.start_new_thread(clientthread, (connectionSocket,))

main()
