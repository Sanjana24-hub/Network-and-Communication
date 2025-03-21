import socket  # Import the socket module to enable network communication


dns_records = {
    "example.com": {"type": "A", "value": "192.168.1.1"},  # A record
    "allis.com": {"type": "CNAME", "value": "example.com"},  # CNAME record (alias)
    "sanjana.com": {"type": "A", "value": "10.0.0.5"},  # A record
    "test.com": {"type": "A", "value": "172.16.0.2"},  # A record
}

# Create a UDP socket for the DNS server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind server to a specific IP (localhost) and port (5054)
server_socket.bind(("localhost", 5054))

print("DNS Server is running on port 5054...")  #Indicate that the server is active

#Server continuously listens for incoming queries
while True:
    # Receive data (query) from the client
    data, client_address = server_socket.recvfrom(1024)  #Receive up to 1024 bytes
    hostname = data.decode().strip()  #Decode the received bytes into a string

    print(f"Received query for: {hostname}")  #Print the received query

    #Check if the hostname exists in the DNS records
    if hostname in dns_records:
        record = dns_records[hostname]

        # Determine the response based on record type
        if record["type"] == "A":
            response = f"A {record['value']}"  # Return IP address for A record
        elif record["type"] == "CNAME":
            response = f"CNAME {record['value']}"  # Return alias for CNAME record
    else:
        response = "ERROR: Host not found"  # If hostname is not in records, return an error

    #Send the response back to the client
    server_socket.sendto(response.encode(), client_address)  # Encode response as bytes and send
