import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
# print(data)
df = pd.DataFrame(data, columns=["col1","col2","col3","col4","col5"]) # with default indexes [0...14]
result =  df

result = df.columns
result = df.head() # default first 5 rows(record)
result = df.head(10)  # first  10 rows
result = df.tail(10)  # last   6 rows

result = df["col1"].head(10)
result = df.col1.head(2)  # same to above line of code
result =df[["col1","col2"]].head(3) # select some specific column and get the head part of it
result =df[["col1","col2"]].tail(3) # select some specific column and get the head part of it

result = df[5:15][["col1", "col2"]].head(8) # slicing by index then select some specific column --> 5 between 15
result = df[5:15][["col1", "col2"]].tail(8) 

result = df >  50  # return a boolean series based on condition
result = df[df > 50]  # filter out the row which meet the condition
result = df[df % 2 == 0] # filter out even number rows 

result = df[df["col1"] > 50] # all cols can be access like this
result = df[df["col1"] > 50][["col1","col2"]]  # filtering and selecting at one time

result = df[(df["col1"] > 40 ) & (df["col2"] <= 75) ] # and operator: &
result = df[(df["col1"] > 40 ) | (df["col2"] <= 75) ] # or operator: |
result = df[(df["col1"] > 60 ) | (df["col2"] > 60) ] 
result = df[(df["col1"] > 45 ) &  (df["col1"] <= 75)]
result = df[(df["col1"] > 45 ) &  (df["col1"] <= 75)][["col1","col2"]]

result = df.query("col1 >=50 & col1 %2 == 0")
result = df.query("col1 >=50 | col1 %2 == 0")[["col1","col2"]] # different way to use query method 

print(result)






