import requests

url="https://localhost:8000/post/"

payload={
    "name":"Sumukh",
    "email":"sumukh@example.com"
}

response = requests.post(url=url, data=payload)

print(response.text)