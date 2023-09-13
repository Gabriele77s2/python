import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve {domain}")

# Example usage:
get_ip_address("example.com")
