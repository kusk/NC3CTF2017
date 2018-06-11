import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('45.63.119.180', 9999)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print("----"*10)
        print('connection from', client_address)
        while True:
            try:
                data = connection.recv(16)
                if data:
                    if data.decode('utf-8').rstrip() == "HELLO":
                        f = open('server_log', 'a')
                        f.write(str(client_address)+" korrekt modtaget \n")
                        f.close()
                        print("? modtaget / sending data back to the client")
                        connection.sendall(str.encode("nc3ctffqqn5ozfjy.onion/2092c7a391323c18413e33f9840c47e6"))
                        connection.close()
                    else:
                        print("Forkert data")
                        f = open('server_log', 'a')
                        try:
                            f.write(str(client_address) + " " +str(data.decode('utf-8').rstrip())+"\n")
                        except:
                            f.write(str(client_address) + " forkert\n")
                        f.close()
                        connection.sendall(str.encode("Forkert"))
                        connection.close()
                    print("----"*10)
                else:
                    break

            finally:
                connection.close()
    except:
        print("error")
