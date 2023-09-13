import socket

def port_scanner(target, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage:
target_ip = "example.com"
ports_to_scan = range(1, 1025)
port_scanner(target_ip, ports_to_scan)
