import socket 

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Receive data from the server

    # data_from_server=cs.recv(100)
    # print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8'))
    readFilePtr = open("in-proj.txt", "r")
    writeFilePtr = open("output.txt", "w")
    count = 0; 
    for line in readFilePtr:
        cs.send(line.encode('utf-8'))
        data_from_server = cs.recv(300)
        data_from_server = data_from_server.decode('utf-8')
        writeFilePtr.write(data_from_server + "\n")
    writeFilePtr.close()

    # close the client socket
    cs.close()
    exit()