import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Send "Hello" to server
    client_socket.sendall("Hello".encode())

    # Receive greeting message from the server side
    server_message = client_socket.recv(1024).decode()
    print(f"Server: {server_message}")

    # Send client's name
    client_name = input("Enter your name: ")
    client_socket.sendall(client_name.encode())

    # Receive final message from the server
    final_message = client_socket.recv(1024).decode()
    print(f"Server: {final_message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
