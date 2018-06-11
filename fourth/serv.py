from socket import *
import _thread

# lavet multithreaded pga. crash snask.

BUFF = 1024
HOST = '45.63.119.180'
PORT = 4444
def response(key):
    return 'Server response: ' + key

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFF)
        if not data: break
        if data.decode('utf-8').rstrip() == "?":
            clientsock.sendall(b"\x57\x4e\x44")
            clientsock.close()
        print(str(addr) + ' recv:' + repr(data))
        print(str(addr))
        if "close" == data.rstrip(): break 

    clientsock.close()
    print(addr, "- closed connection")

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print('waiting for connection... listening on port', PORT)
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        _thread.start_new_thread(handler, (clientsock, addr))
