import requests
from bs4 import BeautifulSoup
import csv

def ExtractTextFromWebPage(url):
    user={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url=url, headers=user).content
    soup = BeautifulSoup(response, "lxml")
    tag=soup.find('p',{"class":"lead"})
    h=tag.find_all("h2")
    content=[span.text for span in h]
    print(content)

    with open('gog.csv','w') as f:
        write=csv.writer(f)
        write.writerows(content)

ExtractTextFromWebPage("https://www.geeksforgeeks.org/")