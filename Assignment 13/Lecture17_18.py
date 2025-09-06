import requests
import re
import os

user= input("Enter image topic: ")

user_agent={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

url=f"https://www.google.com/search?sca_esv=de452c03a6a60aed&rlz=1C1VDKB_enIN1077IN1077&sxsrf=AE3TifPBcIf82Rl-p2gf6-6YbedrDjW2YQ:1757163894600&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmzz3c9iXgklNNbCtRRa3vQiDsiyngHMLCDiFcU14vRYFcn3hDvBtzesTsvCeqVb3Xc1wjI2MTiwr0UAtZV1SeaWYQtAHYGsCkaiqMHRd5y0JCw-KjIg&q={user}&sa=X&ved=2ahUKEwjowP_NmcSPAxVoyzgGHVbvB40QtKgLegQIDxAB&biw=1536&bih=695&dpr=1.25#vhid=OOMgPNdv9As6uM&vssid=mosaic"

response = requests.get(url=url, headers=user_agent).text

pattern="\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"

images=re.findall(pattern,response)

print(images)

down=int(input("Enter number of images to be downloaded: "))

for image in images[:down]:
    if os.path.exists(user)==False:
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)
    image_url=eval(image)[0]
    print(image_url)
    image_name=image_url.split('/')[-1]
    img_data=requests.get(image_url).content
    with open(image_name,'wb') as f:
        f.write(img_data)