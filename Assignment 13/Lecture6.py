import requests

url = "https://imgs.search.brave.com/QA7ihshgYVoPVLka0-osXanBgSEPcDY6TAGZOMbkHqA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTY3/MDI1NDYzNy9waG90/by9zdW5zZXQtdGFs/bC1wb3BsYXItdHJl/ZXMtcGFzdG9yYWwt/d2FsbHBhcGVyLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1V/MDVhT1hSNlhpakpI/eDdXWG96My16VWZm/ZkV6V1JEUjZiWE84/NlR4cUw0PQ"

user={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url=url, headers=user)

pic=response.content

f = open("nature.jpg", "wb")
f.write(pic)
f.close()