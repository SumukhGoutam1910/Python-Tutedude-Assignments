import requests

url="https://localhost:8000/post/"

p={
    "offset": "10",
}

response = requests.post(url=url, params=p)

print(response.text)
print(response.url)