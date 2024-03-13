import pandas as pd
from numpy.random import randn

df =  pd.DataFrame(randn(5, 4), index= ["row1", "row2", "row3", "row4","row5"], columns=['A', 'B', 'C', 'D']) # 4*3 matrix with random numbers --> changes matrix: (5,4)
# result = df

# result = df["A"]
# result2 = df[["A","B"]]

# print(df,"\n")

# print(result,"\n")
# print(result2, "\n")
# print(type(df["A"]))

# row selecting: -row->  loc["row"]   --> loc["row","column"] -only column-> loc[":","column"]
row_res = df.loc["row1"]

# columns : columns=['A', 'B', 'C']
col = df.loc[:,"A"] # get all rows of column A
cols = df.loc[:,["A","B"]] # get columns A and B
cols_apart = df.loc[:, "A":"C" ] # (same slicing) get cols from A to C (included)  --> :, ["A", "B"]
cols_apart_2 = df.loc[:,:"C"] # cols_apart = cols_apart_2

row_col_res = df.loc["row2","A"]

# print(f"Row Selecting:\n{rows}" )

print(df,"\n")
print(f"Row Selecting:\n{row_res}\n") 

print(f"Column Selection:\n{col}\n")
print(f"columns: A-B selecting:\n{cols}\n")
print(f"columns: A-C apart selecting:\n{cols_apart}")
print(f"columns: A-C apart selecting(different format):\n{cols_apart_2}")

print(f"Column and row selecting:\n{row_col_res}\n")
print(type(row_res))  # <class  'pandas.core.series.Series'>

# rows : index= ["row1", "row2", "row3", "row4"] --> eğer index no lar değişmeseydi asagıda : df.loc[0:2,:"C"] diyebilirdik 
# --> yine de index icin:  df.iloc[0:2,:"C"] diyebiliriz
rows = df.loc["row3":"row4",:]
print(f"rows3 and rows4:\n{rows}\n")
rows_2 = df.loc["row1":"row2",:"B"] #  ( ,:"C" -> kolon bastan sona kadar ) --> ( "row1":"row2" -> row1 den row2 ye kadar )
print(f"rows2:\n{rows_2}\n")         # veya -->  df.loc[":"row2","A":"B"] ifadesi aynıdır

# indexes with iloc --> iloc: key, axis --> axis=1: row and axis=0: column , default is axis=0
iloc_rows = df.iloc[2] # default: axis=0 --> [2] contains rows3 and all columns datas (ABC)
print(f" iloc with index:  \n{iloc_rows}\n")  # iloc: return row[index]

row_col = df.loc["row2","D"] 
print(f"row2 intersect D:\n{row_col}")
rows_cols_intercection = df.loc[["row1"], [ "A", "B"]]  # only rows1 and colums A and B
print(f"\nRows and Columns Intersection:\n {rows_cols_intercection}\n")

rows_cols_intercection = df.loc[["row1","row2"], [ "A", "C"]]  #  rows1 and rows2 intersect colums A and B
print(f"\nRows and Columns Intersection:\n {rows_cols_intercection}\n")

# add new columns (with series):
print( "\nAdd New Columns:\n")
df["E"] = pd.Series(randn(5), ["row1","row2","row3","row4","row5"]) # pandas series added
df["F=C+D"] = df["C"] + df["D"]
print(df,"\n")

# df.drop("F=C+D") # real delete is dropna() --> x : axis=0 = row   ||    y : axis=1 = column
delete_view = df.drop("F=C+D", axis=1, inplace= False) # fake delete  --> default: inplace= False
print(f"deleted row:\n{delete_view}\n")
print(f"\nOriginal Dataframe views with inplace = False :\n{df}")

df.drop("F=C+D", axis=1, inplace=True) #  original delete --> axis=1 ,  y(coordinate)-column  --> if we want to delete the original column : inplace = true  
print(f"\nOriginal Dataframe views2 with inplace= True :\n{df}")
