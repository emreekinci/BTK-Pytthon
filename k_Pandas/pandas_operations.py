import pandas as pd
import numpy as np

data = {
    "col1": [1,2,3,4,5],
    "col2": [10,20,13,45,25],
    "col3": ["abc", "bca", "ade", "cba", "dea"]
}

df = pd.DataFrame(data)

def square(x):
    return  x**2

square_2 = lambda x : x * x 

result = df
# print(df)
result_unique = df["col2"].unique() #  get unique values in col2
# print(result_unique)
result_unique_nums = df["col2"].nunique() #  number of unique values in col2
# print(result_unique_nums)
result_value_count = df["col2"].value_counts() #  count the occurrence of each value in col2
# print(result_value_count)
col1_2 = df["col1"] * 2 #   create new column by multiplying col1 with 2
# print(col1_2)
col1_square_apply = df["col1"].apply(square) # apply square function to each element in col1 --> square is a object || there is no parameter 
# print(col1_square_apply)
col1_square_apply = df["col1"].apply(square_2) # or alternative using --> .apply(lambda x: x * x)
# print(col1_square_apply)
col3_str_count = df["col3"].apply(len)
# print(col3_str_count)
df["col3_str_len"] = df["col3"].apply(len)
# print(df)
# print(df.info()) # .columns
# result = df.columns
# result = len(df.columns)
# result = df.index
# result = len(df.index)

# result = df.sort_values(by="col2") # sort dataframe based on col2
# result = df.sort_values(by="col3") # default: ascending = True
# result = df.sort_values("col3", ascending= False)
# print(result)

data_2 = {
    "Ay":["Mayıs", "Haziran", "Nisan", "Mayıs", "Ocak", "Haziran","Mayıs","Nisan","Ocak", "Şubat","Mart","Aralık"],
    "Kategori": ["Elektronik", "Elektronik","Elektronik","Gıda", "Gıda","Gıda","Kitap", "Kitap","Kitap", "Spor","Spor","Kitap"],
    "Gelir": [33,44,54,19,68,77,20,29,64,99,46,19] 
}
df = pd.DataFrame(data_2)
df = df.pivot_table(index="Ay",columns="Kategori", values="Gelir")
print(df)