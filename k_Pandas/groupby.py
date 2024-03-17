import pandas as pd
import numpy as np 

personeller  = {'Calisan': ['Adem Yılmaz', 'Can Eryaman','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
            'Departman':['İK','Bilgi İşlem','Muhasebe','İK','Bilgi İşlem','Muhasebe','Bilgi İşlem'] , 
            'Yaş': [30,25,45,50,23,34,42],
            'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
            'Maaş' : [15000,12000,19000,28000,27000,55000,63000]
} 

df = pd.DataFrame(personeller)
# print(df)

#          Calisan    Departman  Yaş     Semt   Maaş
# 0    Adem Yılmaz           İK   30  Kadıköy  15000
# 1    Can Eryaman  Bilgi İşlem   25    Tuzla  12000
# 2  Hasan Korkmaz     Muhasebe   45  Maltepe  19000
# 3    Cenk Saymaz           İK   50    Tuzla  28000
# 4      Ali Turan  Bilgi İşlem   23  Maltepe  27000
# 5    Rıza Ertürk     Muhasebe   34    Tuzla  55000
# 6    Mustafa Can  Bilgi İşlem   42  Kadıköy  63000

# result = df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 5 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Calisan    7 non-null      object
#  1   Departman  7 non-null      object
#  2   Yaş        7 non-null      int64
#  3   Semt       7 non-null      object
#  4   Maaş       7 non-null      int64
# dtypes: int64(2), object(3)
# memory usage: 412.0+ bytes


result = df["Maaş"].sum()   # 219000
result = df["Maaş"].mean()  # 31285.7142

result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups 
# {('Bilgi İşlem', 'Kadıköy'): [6], ('Bilgi İşlem', 'Maltepe'): [4], ('Bilgi İşlem', 'Tuzla'): [1], 
#('Muhasebe', 'Maltepe'): [2], ('Muhasebe', 'Tuzla'): [5], ('İK', 'Kadıköy'): [0], ('İK', 'Tuzla'): [3]}
# print(result)

# semtler = df.groupby("Semt")
# print(semtler)

# for name,  group in df.groupby("Semt"):
#     print(name) # Kadıköy Maltepe, Tuzla
#     print(group)

# Kadıköy
#        Calisan    Departman  Yaş     Semt   Maaş
# 0  Adem Yılmaz           İK   30  Kadıköy  15000
# 6  Mustafa Can  Bilgi İşlem   42  Kadıköy  63000
# Maltepe
#          Calisan    Departman  Yaş     Semt   Maaş
# 2  Hasan Korkmaz     Muhasebe   45  Maltepe  19000
# 4      Ali Turan  Bilgi İşlem   23  Maltepe  27000
# Tuzla
#        Calisan    Departman  Yaş   Semt   Maaş
# 1  Can Eryaman  Bilgi İşlem   25  Tuzla  12000
# 3  Cenk Saymaz           İK   50  Tuzla  28000
# 5  Rıza Ertürk     Muhasebe   34  Tuzla  55000
    
# for name,  group in df.groupby("Departman"):
#     print(name) # Bilgi İşlem, İK, Muhasebe
#     print(group)

# Bilgi İşlem
#        Calisan    Departman  Yaş     Semt   Maaş
# 1  Can Eryaman  Bilgi İşlem   25    Tuzla  12000
# 4    Ali Turan  Bilgi İşlem   23  Maltepe  27000
# 6  Mustafa Can  Bilgi İşlem   42  Kadıköy  63000
# Muhasebe
#          Calisan Departman  Yaş     Semt   Maaş
# 2  Hasan Korkmaz  Muhasebe   45  Maltepe  19000
# 5    Rıza Ertürk  Muhasebe   34    Tuzla  55000
# İK
#        Calisan Departman  Yaş     Semt   Maaş
# 0  Adem Yılmaz        İK   30  Kadıköy  15000
# 3  Cenk Saymaz        İK   50    Tuzla  28000

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")
result = df.groupby("Departman").sum()
result = df.groupby("Departman")[["Yaş","Maaş"]].mean()

result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Calisan"].count()

result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].max()
result = df.groupby("Departman")["Maaş"].min()["Muhasebe"]

# result = df.groupby("Departman")["Maaş"].agg(np.mean)
result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.min, np.max]).loc["Muhasebe"]

print(result)