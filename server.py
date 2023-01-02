import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    # msg = "Welcome to CS 352!"
    # csockid.send(msg.encode('utf-8'))

    
    readFilePtr = open("in-proj.txt", "r")
    count = 0
    for line in readFilePtr:
        stringReverse = csockid.recv(1024).decode('utf-8')
        stringReverse = stringReverse[::-1]
        stringReverse = stringReverse.lstrip("\n")
        print(stringReverse)
        count += 1
        csockid.send(stringReverse.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()