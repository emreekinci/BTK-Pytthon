import requests # for json
# themoviedb.org
# themoviedb apisini  kullanıyoruz
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi

class theMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3'
        self.api_key =  '01eb58d0f17bb5f43248f42cded7a16f'

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getSearchResult(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&language=en-US&page=1")
        return response.json()
    
movieApi = theMovieDb()

while True:
    secim = input("1- Popüler Movies\n2- Search Movies\n3- Exit\nSeçim: ")
    
    if secim ==  "1":
        movies = movieApi.getPopulars()
        for movie in movies['results']:
            print(movie["title"])
            
    elif secim == '2':
        search_keyword = input("Aramak istediğiniz keyword: ")
        movies = movieApi.getSearchResult(search_keyword)
        for movie in movies['results']:
            print(movie["name"])
    elif secim == '3':
        break
    else:
        print("False choose !!")
        continue
    
    
    
# https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877

# shell: --> movie/top_rated
# curl --request GET \
#      --url 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1' \
#      --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMWViNThkMGYxN2JiNWY0MzI0OGY0MmNkZWQ3YTE2ZiIsInN1YiI6IjY1ZTYwZjQ1YmU3ZjM1MDE3Y2IzNDg4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OivMYfi0b3Osj7lzLqyMg_chmzSGRW1MnG28fgDgj68' \
#      --header 'accept: application/json'

# shell: --> movie/popular           
# curl --request GET \
#      --url 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1' \
#      --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMWViNThkMGYxN2JiNWY0MzI0OGY0MmNkZWQ3YTE2ZiIsInN1YiI6IjY1ZTYwZjQ1YmU3ZjM1MDE3Y2IzNDg4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OivMYfi0b3Osj7lzLqyMg_chmzSGRW1MnG28fgDgj68' \
#      --header 'accept: application/json'

# python: --> movie/popular
# import requests

# url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer 01eb58d0f17bb5f43248f42cded7a16f"
# }

# response = requests.get(url, headers=headers)

# print(response.text)


# search-> keyword
# import requests

# url = "https://api.themoviedb.org/3/search/keyword?page=1"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer 01eb58d0f17bb5f43248f42cded7a16f"
# }

# response = requests.get(url, headers=headers)

# print(response.text)

# https://developer.themoviedb.org/reference/movie-popular-list