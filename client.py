import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def con():
    try:
        s.connect(("localhost", 12000))
    except:
        print('unable to connect')
        exit(0)
    while 1:
        try:
            # str_recv = s.recv(1024)
            # print(str_recv.decode('utf-8'))
            # if str_recv==b'you have disconnect Thankyou':
            #     print("connection terminated")
            #     s.close()
            #     break
            str_send = input('client-->')
            s.send(bytes(str_send, 'utf-8'))
            if str_send.lower() == "exit":
                print("Closing down client")
                break
        except:
            print('connection terminated')
            break
    s.close()
con()