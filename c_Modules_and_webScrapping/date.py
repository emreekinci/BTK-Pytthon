from datetime import datetime
from datetime import timedelta 
# ya da import datetime ile her şeyi dahil et

# from datetime import date
# from datetime import time
# import datetime

#res = dir(datetime)
today = datetime.now()# .today()
# y = today.year
# m = today.month
# d  = today.day
# h = today.hour
# mnt = today.minute
# s = today.second 
result = datetime.ctime(today) # ctime() returns the current time in local
print(result)

# string datas
now_str = today.strftime("%Y-%m-%d %H:%M:%S") # strftime() is used to format dates into strings
print("String Format: ", now_str)

date_my_format = datetime.strftime(today, '%Y %B %A')
print(date_my_format)

t = '03 Mart 2024'
gun, ay, yil = t.split()
print(yil,ay,gun)

t_2 = '16 March  2024 hour 12:58:39'
dt = datetime.strptime(t_2,  "%d %B %Y hour %H:%M:%S") # strptime() is used to convert a string
print(dt)  
dt_res_yr = dt.year
dt_res_mn = dt.month
dt_res_dy = dt.day  
dt_res_hr = dt.hour     
dt_res_mt = dt.minute       
dt_res_sc = dt.second            
print('Year :', dt_res_yr,'\nMonth :', dt_res_mn,"\nDay :", dt_res_dy,"\nHour :", dt_res_hr,"\nMinute :", dt_res_mt,"\nSecond :", dt_res_sc)

birthday = datetime(1999, 3, 16, 12,30,15)
print(f"My birthday {birthday}")
age = today - birthday # time delta
print(f"I am {age.days // 365} years old.")
bt_day = age.days
bt_sec = age.seconds
bt_hr = bt_day * 24    # days -> hours

print(f"{bt_day} days and {bt_sec} seconds are equal to {bt_hr} hours.")

birthday_second = datetime.timestamp(birthday) # timestamp() method converts date and time to seconds 
second_to_dt = datetime.fromtimestamp(birthday_second) 

print(birthday_second, second_to_dt)

future = today + timedelta(days=10)
future_2 = today + timedelta(days=13, hours=10, minutes=10)
print(future, future_2)

past = today - timedelta(days=88, hours=15, minutes=30)
print(past)
