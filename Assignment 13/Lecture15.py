import requests

user= input("Enter image topic: ")

user_agent={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

url=f"https://www.google.com/search?sca_esv=2bd8a92f2f2a46b0&sxsrf=AE3TifPwrIJ5MctYJMv89WuVOhnHhPJKfw:1757160815387&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmzz3c9iXgklNNbCtRRa3vQiDsiyngHMLCDiFcU14vRYFcn3hDvBtzesTsvCeqVb3Xc1wjI2MTiwr0UAtZV1SeaWYQtAHYGsCkaiqMHRd5y0JCw-KjIg&q={user}&sa=X&ved=2ahUKEwibhtuRjsSPAxXtS2wGHWPLMQ0QtKgLegQICRAB&biw=1536&bih=695&dpr=1.25#vhid=cDjIw2A-n4lGTM&vssid=mosaic"

response = requests.get(url=url, headers=user_agent).content
print(response)