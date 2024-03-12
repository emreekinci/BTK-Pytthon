import pandas as pd
import numpy as np 

# data

# pandas_series = pd.Series() # Series([], dtype: object)
# print(pandas_series)
numbers = [20,30,40,50]
pandas_series = pd.Series(numbers) 
# print(pandas_series)
# 0    20
# 1    30
# 2    40
# 3    50
# dtype: int64

letters = ['a','b','c',20] # different type values in list
pandas_series = pd.Series(letters, name='Letter')
# print(pandas_series)
# 0     a
# 1     b
# 2     c
# 3    20
# Name: Letter, dtype: object 

scalar = 5
pandas_series = pd.Series(scalar)
# print(pandas_series)
# 0    5
# dtype: int64

pandas_series = pd.Series(scalar, [0,1,2,3,4])
# print(pandas_series)
# 0    5
# 1    5
# 2    5
# 3    5
# 4    5
# dtype: int64

pandas_series = pd.Series(numbers, ['a','b','c','d'])
# print(pandas_series)
# dtype: int64
# a    20
# b    30
# c    40
# d    50
# dtype: int64

dict = {'a':10, 'b':20, 'c':30, 'd':40} 
pandas_series = pd.Series(dict,  name= "Dictionary")
# print(pandas_series)
# a    10
# b    20
# c    30
# d    40
# Name: Dictionary, dtype: int64

random_numbers = np.random.randint(20,400,12)
pandas_series = pd.Series(random_numbers, name= "Random Numbers (numpy with pandas)")
result = pandas_series[0]
# print(result)        
# 137    

pandas_series = pd.Series([2,3,4,5,6], ['a','b','c','d','e'])
# print(pandas_series['b'])       
# # Output : 3

# print(pandas_series[['a','e']])   
# a    2
# e    6
# dtype: int64
     
# print(pandas_series[0])     # pandas_series[0] --> with FutureWarning (use iloc ) output: 2 
# print(pandas_series[-1])      # output: 6
# print(pandas_series.iloc[0])     
# 2     

# print(pandas_series.iloc[1])   # # second element acces
# output: 3

# print(pandas_series[:2])         #  first two elements access
# a    2
# b    3
# dtype: int64

# print(pandas_series[-2:])        #  last two elements access
# d    5
# e    6
# dtype: int64

# print(pandas_series['d'])         # label based access
# 5
# print(pandas_series.loc['d'])       # loc is more safer than using labels because it gives key error if the label not found in dataframe
# 5

# print(pandas_series[['a','b','c','d','f']])        # KeyError: "['f'] not in index"
# if you wont ignore  the key error use this code instead of above line 
# print(pandas_series.reindex (['a', 'b', 'c', 'd' ,'f']))   

# print(pandas_series[1:3])       # slicing 
# a    3
# b    4
# Name: b, dtype: int64

# general using examples:
dimension = pandas_series.ndim
shape = pandas_series.shape
dtype = pandas_series.dtype
sqrt = np.sqrt(pandas_series)

condition = pandas_series >= 3
odd_vals = pandas_series %2 == 0
even_vals = ~odd_vals
short_odds = pandas_series[odd_vals]
short_evens = pandas_series[even_vals]
print(f"dimension: {dimension}\nshape: {shape}\ndtype: {dtype}\nsum: {pandas_series.sum()}\nmax: {pandas_series.max()}\n2x pandas datas: \n{2*pandas_series}\nsqrt: {sqrt}\ncondition: {condition} ")
print(f"\nodd values(boolean): \n{odd_vals}\neven values(boolean): {even_vals}\nodd  values: \n{short_odds}\neven values: \n{short_evens}\n")

# print(pandas_series.iloc[:-1]) # all elements except the last one
# a    2
# b    3
# c    4
# d    5

# print(pandas_series[::2])       # select every 2nd row starting from index 0 -> [2, 4]
# a    2
# c    4
# e    6
# dtype: int64          
     
# PART-2 
# odds_index =  result % 2 == 0
# print(pandas_series)
# print(f" The first number in the series is :{result}")

# even odd numbers
res1 = []
res2 = [] 
df_res1 = []
df_res2 = []

for i in  range(len(random_numbers)): # odd
    if random_numbers[i] % 2 == 0:
        res1.append(random_numbers[i])
        # print(res1)
    else:
        res2.append(random_numbers[i])
        # print(res2)
# print(f"\nodds series: {res1}")
# print(f"\nevens series: {res2}", "\n")

for i in range(len(res1)): # even
    if len(res1) >= 0 :
        df_res1.append({'Number': res1[i], 'Label': 'Odd'})
        #df_res2.append({'Number': res2[i], 'label': 'Even})
    else:
        print("odd numbers no generate !!")
        
# print(df_res1, "\n")
# pandas_res1 = pd.Series(df_res1, name= "Odd Numbers")
# print("pandas result(odds): \n", pandas_res1)

# print(pandas_res1, "\n")

# try excepte alinabilir
for i in range(len(res2)):
    if len(res2) >= 0 :
        df_res2.append({'Number': res2[i], 'Label': 'even'}) 
    else:
        print("even numbers no generate !!")
        
# print(df_res2, "\n")
# pandas_res2 = pd.Series(res2, name='Even Numbers')
# print("pandas result:(evens) \n", pandas_res2)

opel_cars_2022 = pd.Series([850,760,780,980,465,988,1300], ["astra","corsa","mokka","insignia","Grandland","combo","crossland"])      
opel_cars_2024 = pd.Series([2850,1700,1657,1350,1455,1907,1900], ["","corsa","mokka","insignia","combo","Grandland","crossland"])   # first element is NaN   
total = opel_cars_2022 + opel_cars_2024
# print(total)
print(f"astra: {total["astra"]}")
print(f"corsa: {total["corsa"]}")
print(f"mokka: {total["mokka"]}")
print(f"insignia: {total["insignia"]}")
print(f"Grandland: {total["Grandland"]}")
print(f"combo: {total["combo"]}")
print(f"crossland: {total["crossland"]}")
print(f"\ndata_type: {type(total)}") # data_type: <class 'pandas.core.series.Series'>
