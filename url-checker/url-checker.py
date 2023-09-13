import requests

url = input("Enter URL: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("URL is reachable and returns a valid response.")
    else:
        print("URL is reachable, but the response is not valid.")
except requests.ConnectionError:
    print("URL is not reachable.")
