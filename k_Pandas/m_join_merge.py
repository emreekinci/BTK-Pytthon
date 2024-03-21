import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName':  ['John', 'Jane','Tom','Alice'],
#     'LastName': ['Doe', 'Smith','Nyan','Cat'] ,
# }

# orders = {
#     'OrderId': [10,11,12,13,14] ,
#     'CustomerId': [1,12,2,32,4] ,
#     'OrderDate': ['2024-02-07','2024-03-18','2021-09-10','2022-07-15','2023-10-22']
# }

# # df_customers = pd.DataFrame(customers, columns=list(customers.keys()))

# df_customers = pd.DataFrame(customers, columns= ['CustomerId','FirstName','LastName'])
# df_orders = pd.DataFrame(orders, columns= ['OrderId','CustomerId','OrderDate']) 

# print (f"customers: \n{df_customers}\n")
# print (f"orders: \n{df_orders}")

# result_inner = pd.merge(df_customers,df_orders, how="inner")
# print(f"\nInner Join Result': {result_inner}\n")

# result_left = pd.merge(df_customers,df_orders, how="left")
# print(f"\nLeft Join Result': {result_left}\n")

# result_right = pd.merge(df_customers,df_orders, how="right")
# print(f"\nRight Join Result': {result_right}\n")

# result_outer = pd.merge(df_customers,df_orders, how="outer")
# print(f"\nOuter Join Result': {result_outer}\n")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName':  ['John', 'Jane','Tom','Alice'],
    'LastName': ['Doe', 'Smith','Nyan','Cat'] ,
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName':  ['Emre', 'Jason','Tom','Ally'],
    'LastName': ['Ekinci', 'Sandler','Clancy','Mendy'] ,
}

df_customersA = pd.DataFrame(customersA, columns= ['CustomerId','FirstName','LastName']) # axis=0 --> row
df_customersB = pd.DataFrame(customersB, columns= ['CustomerId','FirstName','LastName'])

result_conct_row = pd.concat([df_customersA,df_customersB]) #default axis=0
print(f"axis=0-row: \n{result_conct_row}\n")

result_conct_col = pd.concat([df_customersA,df_customersB],axis=1) # cola,colb
print(f"axis=1-col: \n{result_conct_col}\n")
