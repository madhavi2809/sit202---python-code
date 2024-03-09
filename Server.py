from socket import *

# Dictionary to store domain name to IP mappings
DNS_DICTIONARY = {
    'google.com': '142.250.206.132',
    'lucid.app': '[23.58.93.138] and [23.58.93.107]',
    'ontrack.chitkara.edu.in': '34.224.135.64',
    'deakin.edu.au': '[104.18.13.173] and [104.18.12.173]'
}


def dns_server():
    # Create a TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Bind the socket to localhost and port 53 (DNS default port)
    server_socket.bind(('localhost', 2150))

    # Listen for incoming connections
    server_socket.listen(1)

    print("DNS Server is running...")

    while True:
        # Accept incoming connection
        conn, addr = server_socket.accept()

        # Display connection information
        print(f"Connection from {addr}")

        # Receive data from client (domain name)
        data = conn.recv(1024).decode().strip()
        print(f"Query received: {data}")

        # Lookup IP address for the requested domain name
        if data in DNS_DICTIONARY:
            ip_address = DNS_DICTIONARY[data]
        else:
            ip_address = "Domain not found"

        # Send the IP address back to the client
        conn.send(ip_address.encode())

        # Close the connection
        conn.close()


if __name__ == "__main__":
    dns_server()
