import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server is listening on the port number 12345...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive "Hello" from client
    client_message = conn.recv(1024).decode()
    print(f"Client: {client_message}")

    # Send greeting message and ask for the username
    conn.sendall("Hello, I hope you are fine. What’s your name?".encode())

    # Receive name from the client
    client_name = conn.recv(1024).decode()
    print(f"Client's Name: {client_name}")

    # Send personalized welcome message
    welcome_message = f"Hello {client_name}, Welcome to SIT202: Network and Communication"
    conn.sendall(welcome_message.encode())

    conn.close()
    server_socket.close()
if __name__ == "__main__":
    start_server()
