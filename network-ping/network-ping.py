import os

def ping(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{host} is up")
    else:
        print(f"{host} is down")

# Example usage:
ping("google.com")
