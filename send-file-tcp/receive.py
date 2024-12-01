import socket

def receive_file(filename, port, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print("Server listening on port:", port)

    conn, addr = s.accept()
    print("Connected to:", addr)

    received_password = conn.recv(1024).decode()
    if received_password != password:
        conn.sendall("Authentication failed".encode())
        conn.close()
        print("Authentication failed.")
        return
    else:
        conn.sendall("Authenticated".encode())

    # receive file
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    conn.close()
    print("File received successfully")

if __name__ == "__main__":
    filename = "received_file"
    port = 9091
    password = "password" 
    receive_file(filename, port, password)
