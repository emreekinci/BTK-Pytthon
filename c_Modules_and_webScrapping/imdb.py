import requests
from bs4 import BeautifulSoup

import pandas as pd
# #yöntem 1
# url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# # taklit: to mimic a browser
# headers = { 
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
# }

# html = requests.get(url, headers).content # sayfadan->incele->network->toptv/?->headers: altından copy user agent  
# print(html) # <Response [403]> : tarayıcı olmadığımız icin hata

#  yöntem 2
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# # Use a proxy server
# # proxy = {
# #     "http": "http://your_proxy_server_address:your_proxy_server_port",
# #     "https": "https://your_proxy_server_address:your_proxy_server_port"
# # }

# Mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.content
    #print(html) # all html page content
    soup = BeautifulSoup(html, "html.parser") # parse the content with Beautiful Soup
    liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li",limit=100)
    #print(liste)
    for item in liste:
        film_name = item.find("h3",{"class":"ipc-title__text"}).text
        puan = item.find("span", {"class":"ipc-rating-star"}).text
        print(film_name, puan)
    
except requests.exceptions.HTTPError as e:
    print(f"An error occurred: {e}")



# non relation for context
# soup = BeautifulSoup(html, "html.parser") # parse the content with Beautiful Soup
# print("Title of the webpage: ", soup.title.string)
# movies = soup.find_all('td', class_='titleColumn') # find all elements with class name 'titleColumn'

# movie_list = []
# for movie in movies:
#     title = movie.a.text                
#     year = movie['data-year']           
#     rating = movie.strong.text[1:]          
#     movie_dict = {'title': title, 'year': year, 'rating': rating}
#     movie_list.append(movie_dict)


# df = pd.DataFrame(movie_list)
# print("\n")
# print(df)   




