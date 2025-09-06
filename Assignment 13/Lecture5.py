import requests

url = "https://localhost:8000/helloworld/"

user={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response=requests.get(url=url, headers=user)
print(response.request.headers)