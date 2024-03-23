import pandas as pd
import numpy as np

df = pd.read_csv("C:/w_emre_desktop/Roof/BTK/Python/k_Pandas/nba.csv")

# 1- Ilk 10 kayıt
result = df.head(10)
# print(result)

# 2- Toplam kayıt sayısı
result = len(df)
result = len(df.index) # alternative way to get the total number of rows in a dataframe
# print(result)

# 3- Tüm oyuncuların toplam yaş ortalamaları ?
result = df["Age"].mean()
# print(result)

# 4- En yüksek yaş kaçtır ?
result = df["Age"].max()
# print(result)

# 5- En yüksek yaş kaçtır ve bu oyuncunun ismi ve yaşı nedir?
result = df[df["Age"] == df["Age"].max()][["Player", "Age"]].iloc[0]
# print(result)

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımlar nelerdir?
result = df[(df["Age"]>=20) & (df["Age"]<25)][["Player", "Tm", "Age"]].sort_values(by="Age").head(50)
# print(result)

# 7- Bojan Bogdanovic\bogdabo02 hangi takımda oynuyor?
result = df[df["Player"]=="Alex Abrines"][["Player","Tm"]].iloc[0]
# print(result)

# 8- Takımlara göre oyuncuların ortalama yaşları nedir?
result = df.groupby("Tm").mean(["Age"])["Age"]
# print(result)

# 9- Kaç farklı takım vardır
# result = len(df.groupby("Tm"))
# result = df["Tm"].unique() 
# ['OKC' 'BRK' 'MIA' 'ORL' 'MIN' 'SAS' 'BOS' 'NOP' 'POR' 'PHI' 'HOU' 'IND'
#  'MIL' 'TOR' 'CHI' 'DEN' 'TOT' 'ATL' 'CHO' 'NYK' 'LAL' 'DAL' 'WAS' 'GSW'
#  'PHO' 'LAC' 'SAC' 'DET' 'UTA' 'MEM' 'CLE']

result = df["Tm"].nunique() # 31 --> len(df["Tm"].unique())
# print(result)

# 10- Her takımda kaç oyuncu oynamaktadır?
result = df["Tm"].value_counts()
# print(result)

# 11- İsmi içinde and geçen kayıtları getir
# for NaN values -> df = df.dropna() or df.dropna(inplace= True)
# df = df.dropna()
# result = df[df["Player"].str.contains("and")]["Player"]
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Player"].apply(str_find)]["Player"]
print(result)
