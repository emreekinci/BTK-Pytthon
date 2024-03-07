import math
import time

# Bir fonksiyonu çagırdıgımızda otomatik olarak diger islemleri de tetikliyor olacagiz 

def my_decorator(func):
    def wrapper(name): # 1- (), 2- name
        print("Fonksiyon oncesi islemler.")
        func(name) # 2- name
        print("Fonksiyondan sonraki islemler.")
    return wrapper

def sayHello():
    print("Hello")
    
@my_decorator # sayHello2 referansini my_decorator a gonder demek    
def sayHello2(name):
    print(f"Hello2, {name}")
    
def sayGreeting():
    print("Greeting")

# -1-
# sayHello = my_decorator(sayHello) # using
# sayHello() # call

# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()

# -2-
sayHello2("Emre")

def calculate_time(func):
    def inner_two( *args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " + str(finish-start)+ " saniye surdu.")
    return inner_two

@calculate_time
def count():
    counter=0
    for i in range(10000):
        counter+=i
    return counter

@calculate_time
def usalma(a,b):
    print(pow(a,b))
  
@calculate_time    
def faktoriyel_al(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)
    
usalma(2,3)
faktoriyel_al(5)
count()
toplama(10,20)

        

