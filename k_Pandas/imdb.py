import pandas as pd

df = pd.read_csv("C:\w_emre_desktop\Roof\BTK\Python\k_Pandas\IMDB_Top_250_Movies.csv")

# 1- Dosya Hakkındaki bilgiler

result = df
# result = df.columns
# Index(['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time',
#        'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers'],
#       dtype='object')

# result  = df.info
# [250 rows x 13 columns]>
#print(result)

# 2- ilk 5 kayıt
result = df.head()
# print(result)

# 3- ilk 10 kayıt
result = df.head(10)
# print(result)

# 4- son 10 kayıt
result = df.tail(10) # default 5
# print(result)

# 5- sadece name kolonunu al
result  = df['name']
# print(result)

# 6- sadece name kolonunu içerem ilk 5 ve son 10 kayıt
first_five = df["name"].head()
last_ten = df["name"].tail(10)

# print(first_five)
# print(last_ten)

# 7- sadece name ve rating kolonunu içeren ilk 10 kayıt
combined_operation = df[["name", "rating"]].head(10)
# print(combined_operation)

# 5- sadece name ve rating kolonunu içeren son 20 kayıt
name_rate = df[["name","rating"]].tail(20)
# print(name_rate)

# 9- sadece name ve rating kolonunu içeren ikinci 10 kaydı al
second_ten_record = df[10:][["name","rating"]].head(10)
# print(second_ten_record)

# 10- sadece name, rating,casts ve year iceren ve rating in 8 den yılın da 2001 den büyük olduğu kayıtları al
big_rated=df[(df["rating"] >= 8.0) & (df["year"] > 2001)][["name","rating","year"]].head(50)
# print(big_rated)

# 11- yayın tarihi 2016 ve 2019 aralığında olan filmlerin isimlerini ve tarihleri süreleriyle beraber getir
#Index(['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time',
#       'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers'],
col_names = df.columns #
# print(col_names) 
year_cond = df[(df["year"] >= 2016) & (df["year"] <= 2019) ][["name","year","run_time"]]
print(year_cond)

# 33                                    Parasite  2019   2h 12m
# 62                      Avengers: Infinity War  2018   2h 29m
# 65           Spider-Man: Into the Spider-Verse  2018   1h 57m
# 72                                        Coco  2017   1h 45m
# 74                                       Joker  2019    2h 2m
# 77                           Avengers: Endgame  2019    3h 1m
# 81                                  Your Name.  2016   1h 46m
# 87                                   Capernaum  2018    2h 6m
# 122                                       1917  2019   1h 59m
# 124                                     Dangal  2016   2h 41m
# 132                                 Green Book  2018   2h 10m
# 164  Three Billboards Outside Ebbing, Missouri  2017   1h 55m
# 179                                      Klaus  2019   1h 36m
# 191                              Hacksaw Ridge  2016   2h 19m
# 209                             Ford v Ferrari  2019   2h 32m
# 215                                      Logan  2017   2h 17m
# 238                             The Handmaiden  2016   2h 25m

# 12- yayın tarihi 2016 ve 2019 aralığında olmayan filmlerin isimleri, tarihlerini ve sürelerini beraber getir
# year_cond = df[(df["year"] >= 2016) & (df["year"] <= 2019) ][["name","year","run_time"]]
year_not_cond = df[(df["year"] < 2016) | (df["year"] > 2019)][["name", "year","run_time","rank"]].head(50)
# print(year_not_cond)

# 0                            The Shawshank Redemption  1994   2h 22m
# 1                                       The Godfather  1972   2h 55m
# 2                                     The Dark Knight  2008   2h 32m
# 3                               The Godfather Part II  1974   3h 22m
# 4                                        12 Angry Men  1957   1h 36m
# 5                                    Schindler's List  1993   3h 15m
# 6       The Lord of the Rings: The Return of the King  2003   3h 21m
# 7                                        Pulp Fiction  1994   2h 34m
# 8   The Lord of the Rings: The Fellowship of the Ring  2001   2h 58m
# 9                      The Good, the Bad and the Ugly  1966   2h 58m
# 10                                       Forrest Gump  1994   2h 22m
# 11                                         Fight Club  1999   2h 19m
# 12              The Lord of the Rings: The Two Towers  2002   2h 59m
# 13                                          Inception  2010   2h 28m
# 14     Star Wars: Episode V - The Empire Strikes Back  1980    2h 4m
# 15                                         The Matrix  1999   2h 16m
# 16                                         Goodfellas  1990   2h 25m
# 17                    One Flew Over the Cuckoo's Nest  1975   2h 13m
# 18                                              Se7en  1995    2h 7m
# 19                                      Seven Samurai  1954   3h 27m
# 20                              It's a Wonderful Life  1946   2h 10m
# 21                           The Silence of the Lambs  1991   1h 58m
# 22                                        City of God  2002   2h 10m
# 23                                Saving Private Ryan  1998   2h 49m
# 24                                       Interstellar  2014   2h 49m
# 25                                  Life Is Beautiful  1997   1h 56m
# 26                                     The Green Mile  1999    3h 9m
# 27                 Star Wars: Episode IV - A New Hope  1977    2h 1m
# 28                         Terminator 2: Judgment Day  1991   2h 17m
# 29                                 Back to the Future  1985   1h 56m
# 30                                      Spirited Away  2001    2h 5m
# 31                                        The Pianist  2002   2h 30m
# 32                                             Psycho  1960   1h 49m
# 33                                           Parasite  2019   2h 12m
# 34                             Léon: The Professional  1994   1h 50m
# 35                                      The Lion King  1994   1h 28m
# 37                                 American History X  1998   1h 59m
# 38                                       The Departed  2006   2h 31m
# 39                                 The Usual Suspects  1995   1h 46m
# 40                                       The Prestige  2006   2h 10m
# 41                                           Whiplash  2014   1h 46m
# 42                                         Casablanca  1942   1h 42m
# 43                             Grave of the Fireflies  1988   1h 29m
# 44                                           Harakiri  1962   2h 13m
# 45                                   The Intouchables  2011   1h 52m
# 46                                       Modern Times  1936   1h 27m
# 47                       Once Upon a Time in the West  1968   2h 45m
# 48                                        Rear Window  1954   1h 52m
# 49                                    Cinema Paradiso  1988   2h 35m


