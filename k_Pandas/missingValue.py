import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5,3)
df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns=['c1', 'c2','c3'])
# print(df)
df = df.reindex(['a','b','c','d','e','f','g','h'])

# add new column
newColumn = [np.nan, 25 , np.nan, 78, np.nan, 46, 88, np.nan] # new column values with NaN values
df["c4"] = newColumn

result = df

# delete column/s --> axis = 1
result = df.drop("c1", axis=1)           # delete  column c1
result = df.drop(["c1","c2"], axis=1)    # delete multiple columns at once 


# delete row/s --> axis = 0
# result = df.drop("b", axis=0)          # delete rows b, d and g
result = df.drop(["b","d","g"], axis=0)  # delete rows b, d and g

# isnull()
# result = df.isnull()                   # True and False values  --> True (null values return ) or False (non-null values return)
# result = df.notnull()                  # negation of isnull(), returns true where there is no null value
result = df.isnull().sum(axis=0) # return the number of missing values in each column
result = df["c1"].isnull().sum(axis=0)   # check for missing values only in column c1 --> c1 = 3 missing value

# print(df)                              # added new column : c4
result = df[df["c4"].isnull()]
result = df[df["c4"].isnull()]["c4"]     # only c4 column from the dataframe df where it has a missing value --> returns series object
result = df[df["c4"].notnull()]["c4"] 

# dropna -->  remove rows containing NA/NaN values  --> axis=0 : rows // axis= 1 : columns
result = df.dropna()                     #  drop all rows containing NA values --> default axis = 0 for rows
result = df.dropna(axis= 1)              #  drop all columns containing NA values --> default axis = 0 for columns

result = df.dropna(how= "any")           # drop any row that contains at least one NA value (any: all rows are dropped if any row has a NaN)
result = df.dropna(how= "all")           # how = ‘all’ : If all row including NaN values then it will be removed from DataFrame. 

result = df.dropna(thresh= 3)            # drop if more than  two NA values are present in a row --> at least 3 normal value
result = df.dropna(thresh= 5, axis=1)    # for rows:  3 NaN / 5 normal  -->   drop if more than 3 NaN values  --> at least 5 normal value
# spesific search NaN  or NA values --> subset = []
print(df)
result = df.dropna(subset =  ["c1", "c2","c3"], how="any")   # 1 NaN value in any of these columns will drop the row
result = df.dropna(subset =  ["c1", "c2","c3"], how="all")   # if c1, c2, c3 is NaN  then it will be dropped for relevant row/s
# result = df.dropna(subset =  ["c1", "c2"], how="all")    
# result = df.dropna(subset = ["c1","c4"], how= "any")   # 1 NaN  value in either c1 or c4 will drop that row

# fillna  method to replace NaN values --> method = {ffill | backfill}
result = df.fillna(value =  99)            # fills NaN values with a specified value--> 99
# result = df.fillna(value =  " ")    
# result = df.fillna(value =  "Bos")   

result = df.sum() # column by column sum
result = df.sum().sum() # all columns sum
result = df.size # 8x4 : 32
result = df.isnull().sum()
# c1    3
# c2    3
# c3    3
# c4    4
# dtype: int64
result = df.isnull().sum().sum() # 3+3+3+4 = 13
 
def average(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum() # 32 -  13
    return toplam / adet

result = df.fillna(value=average(df))        # for all values
 
print(result)
