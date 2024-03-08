import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

headers = {
    
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" 
}

# response = requests.get(url, headers=headers)
# html = response.content
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'html.parser')  # parse the content with python built in HTML parser
# print(html)
liste = soup.find_all("li", {"class":"column"}, limit=10)
# print(liste)
count=1
for li in liste:
    print(f"{count}. Product")
    link = li.a.get("href")
    p_name = li.a.h3.text
    
    images = li.find("img", {"class":"cardImage"}).get("data-images").split(",") # .[0], .[1], .[2]
    print(f"count image: {len(images)}\n----------")
    for url_image in range(len(images)):
        print(f"{url_image}. image  url : {images[url_image]}")
    #print("image: {images[i]}")
    price = li.find("div",{ "class": "priceContainer" }). find_all("span") # indirimli üründe 3 span, indirimsiz 2 span var-> son span değerini alıyoruz
    net_price = price[-1].ins.text.strip("TL") # only numeric  value
    print(f"----------\nlink: {link}\nproduct name: {p_name}\nnet price: {net_price}\n******************")
    count+=1
    
