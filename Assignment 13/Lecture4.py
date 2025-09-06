import requests

url="https://localhost:8000/helloworld/"

response = requests.get(url=url)
print(response)
print(dir(response))
print(response.request.headers)
print(response.status_code)