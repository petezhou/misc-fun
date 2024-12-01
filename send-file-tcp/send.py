import socket
import sys

def send_file(filename, host, port, password):
    with open(filename, 'rb') as f:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(password.encode())
        response = s.recv(1024).decode()
        if response != "Authenticated":
            print("Authentication failed!")
            return
        
        while True:
            data = f.read(1024)  
            if not data:
                break  
            s.sendall(data)
        s.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    host = sys.argv[2]
    port = sys.argv[3]
    password = "password"
    send_file(filename, host, port, password)
