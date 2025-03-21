import socket
server_address = ("localhost", 5054)
while True:
    try:
        # Get hostname input
        hostname = input("Enter a hostname (or 'exit' to quit): ").strip()

        if not hostname:
            print("Hostname cannot be empty! Please enter a valid hostname.")
            continue
        if hostname.lower() == "exit":
            print("Exiting DNS Client...")
            break
        # Create a UDP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send the query to the server
        client_socket.sendto(hostname.encode(), server_address)
        # Receive and display response
        response, _ = client_socket.recvfrom(1024)
        print(f"Response: {response.decode()}")

        client_socket.close()

    except KeyboardInterrupt:
        print("\nDNS Client interrupted. Exiting...")
        break
