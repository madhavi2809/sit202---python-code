from socket import *


def dns_client(domain_name):
    # Create a TCP socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 2150))

    # Send the domain name query to the server
    client_socket.send(domain_name.encode())

    # Receive the response from the server
    ip_address = client_socket.recv(1024).decode()

    # Print the response
    print(f"IP Address for {domain_name}: {ip_address}")


if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    dns_client(domain_name)
