import pandas as pd

# s1 = pd.Series([0, 2, -3, 4])
# s2 = pd.Series([0, 3, 7, 9])

# data = dict(apples=s1, oranges=s2) # key = column
# df = pd.DataFrame(data)
# print(df)

df = pd.DataFrame()
# print(df)
# Empty DataFrame
# Columns: []
# Index: []

df = pd.DataFrame([1,3,5,7,9])
# print(df)
#    0
# 0  1
# 1  3
# 2  5
# 3  7
# 4  9

list = [["Ali", 12], ["Emre", 24], [ "Mehmet", 59],["Çınar", 46]]
dict = {"Name": ["Ahmet","Emre", "Mehmet", "Çınar"], "Age": [12,24,59,46]}
dict_list = [{"Name":"Ali","Age":22},
             {"Name":"Emre","Age":24},
             {"Name":"Mehmet","Age":19},
             {"Name":"Çınar","Age":57}
             ]

# df2 = pd.DataFrame([["Ali", 120], ["Emre", 120], [ "Mehmet", 80],["Çınar", 60]])
df2 = pd.DataFrame(list, index=[1,2,3,4], columns=['Name', 'Age']) # dtype = float --> ValueError
# print(df2)
#  output -> without index param:
#      Name  Age
# 0     Ali   12
# 1    Emre   24
# 2  Mehmet   59
# 3   Çınar   46

# with index and dtype(error)
#      Name  Age
# 1     Ali   12
# 2    Emre   24
# 3  Mehmet   59
# 4   Çınar   46

df3  =  pd.DataFrame(dict, index=["212","352","1657","254"])
# print(df3)
#      Name  Age
# 0   Ahmet   12
# 1    Emre   24
# 2  Mehmet   59
# 3   Çınar   46

df4 = pd.DataFrame(dict_list,index=["212","352","1657","254"]) # index=range(1,5)
print(df4)


















