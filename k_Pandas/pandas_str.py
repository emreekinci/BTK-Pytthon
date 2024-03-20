import pandas as pd

data = pd.read_csv("nba.csv")
# print(data)
# print(data.info())

# befor data info
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Rk           664 non-null    int64
#  1   Player       664 non-null    object
#  2   Pos          664 non-null    object
#  3   Age          664 non-null    int64
#  4   Tm           664 non-null    object
#  5   G            664 non-null    int64
#  6   MP           664 non-null    int64
#  7   PER          664 non-null    float64
#  8   TS%          660 non-null    float64
#  9   3PAr         660 non-null    float64
#  10  FTr          660 non-null    float64
#  11  ORB%         664 non-null    float64
#  12  DRB%         664 non-null    float64
#  13  TRB%         664 non-null    float64
#  14  AST%         664 non-null    float64
#  15  STL%         664 non-null    float64
#  16  BLK%         664 non-null    float64
#  17  TOV%         660 non-null    float64
#  18  USG%         664 non-null    float64
#  19  Unnamed: 19  0 non-null      float64
#  20  OWS          664 non-null    float64
#  21  DWS          664 non-null    float64
#  22  WS           664 non-null    float64
#  23  WS/48        664 non-null    float64
#  24  Unnamed: 24  0 non-null      float64
#  25  OBPM         664 non-null    float64
#  26  DBPM         664 non-null    float64
#  27  BPM          664 non-null    float64
#  28  VORP         664 non-null    float64
# dtypes: float64(22), int64(4), object(3)
# memory usage: 150.6+ KB

# data = data.dropna()
# data.dropna(inplace=True) # NaN values deleted at the original dataframe

# after data info
# print(data)
# print(data.info())

# Columns: [Rk, Player, Pos, Age, Tm, G, MP, PER, TS%, 3PAr, FTr, ORB%, DRB%, TRB%, AST%, STL%, BLK%, TOV%, USG%, Unnamed: 19, OWS, DWS, WS, WS/48, Unnamed: 24, OBPM, DBPM, BPM, VORP]
# Index: []
# <class 'pandas.core.frame.DataFrame'>
# Index: 0 entries
# Data columns (total 29 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Rk           0 non-null      int64
#  1   Player       0 non-null      object
#  2   Pos          0 non-null      object
#  3   Age          0 non-null      int64
#  4   Tm           0 non-null      object
#  5   G            0 non-null      int64
#  6   MP           0 non-null      int64
#  7   PER          0 non-null      float64
#  8   TS%          0 non-null      float64
#  9   3PAr         0 non-null      float64
#  10  FTr          0 non-null      float64
#  11  ORB%         0 non-null      float64
#  12  DRB%         0 non-null      float64
#  13  TRB%         0 non-null      float64
#  14  AST%         0 non-null      float64
#  15  STL%         0 non-null      float64
#  16  BLK%         0 non-null      float64
#  17  TOV%         0 non-null      float64
#  18  USG%         0 non-null      float64
#  19  Unnamed: 19  0 non-null      float64
#  20  OWS          0 non-null      float64
#  21  DWS          0 non-null      float64
#  22  WS           0 non-null      float64
#  23  WS/48        0 non-null      float64
#  24  Unnamed: 24  0 non-null      float64
#  25  OBPM         0 non-null      float64
#  26  DBPM         0 non-null      float64
#  27  BPM          0 non-null      float64
#  28  VORP         0 non-null      float64
# dtypes: float64(22), int64(4), object(3)
# memory usage: 0.0+ bytes

# data["Player"] = data["Player"].str.upper()
# data["Player"] = data["Player"].str.lower()
# data["index"] = data["Player"].str.find('a')
# data = data["Player"].str.contains('Steven Adams')

# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5    False
# 6    False
# 7    False
# 8    False
# 9    False
# Name: Player, dtype: bool

# data = data[data["Player"].str.contains('Steven Adams')]
# data = data["Player"].str.replace(' ','-')
# data[['Name','SurName_ShortName']] = data['Player'].loc[data['Player'].str.split().str.len()==2].str.split(expand=True)

print(f"Before: \n{data.head(10)}\n")
# print(data.info())

data.drop("Unnamed: 19", axis=1, inplace=True) # for deleting original df --> inplace = True
data.drop("Unnamed: 24", axis=1, inplace=True) # for deleting original df --> inplace = True
print
print(f"After drop: \n{data.head(10)}")


# example: drop list
# drop cols: "Unnamed: 19", "OWS", "DWS", "WS/48", "OBPM", "DBPM", "VORP"
# cols_to_drop = ["Unnamed: 19","OWS","DWS","WS/48","OBPM","DBPM","VORP"]
# for col in cols_to_drop:
# 	if col in data.columns:
# 		data = data.drop([col], axis=1)

# kaggle link 
# https://www.kaggle.com/code/kerneler/starter-2017-2018-nba-player-stats-4ec8b612-e/input

# correlation analysis and the others things Exception
# https://www.kaggle.com/code/kerneler/starter-2017-2018-nba-player-stats-4ec8b612-e/notebook

# By the way for nba_view.txt :
# extensions --> CSV to Table --> searchbar: >convert to table from CSV