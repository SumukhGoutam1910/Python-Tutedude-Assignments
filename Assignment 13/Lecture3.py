import urllib.request, urllib.parse, urllib.error

url="https://127.0.0.1:8000/helloworld/"
uh=urllib.request.urlopen(url)
for line in uh:
    print(line.decode().strip())