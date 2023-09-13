import requests

long_url = input("Enter the long URL: ")

api_url = "https://api-ssl.bitly.com/v4/shorten"
access_token = "YOUR_ACCESS_TOKEN"  # Replace with your actual access token

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

payload = {
    "long_url": long_url
}

response = requests.post(api_url, json=payload, headers=headers)

if response.status_code == 200:
    short_url = response.json()["id"]
    print(f"Short URL: {short_url}")
else:
    print("Error generating short URL")
