#import sqlite3
import pandas as pd

# df  = pd.read_json('users.json')
# df = pd.read_csv('player_data.csv')
# df = pd.read_excel("sample.xlsx")

con = sqlite3.connect("sample.db") # samplee.db : Database name
df = pd.read_sql_query("SELECT * FROM students", con)
print(df)

# terminal --> pip install pysqlite3
