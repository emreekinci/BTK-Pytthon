# import math
# import math as m dersek math yerine : " m " kullanırız..
# # value = dir(math)
# # print(value)

# # value_2 = help(math)
# # print(value_2)

# value_3 = help(math.factorial)
# print(value_3)

# value_4 = math.factorial(5)
# print(value_4)

# value_5 = math.sqrt(49)
# print(value_5)

# value_6 = math.floor(4.9)
# value_7 = math.ceil(4.1)
# print(f"floor : {value_6}")
# print(f"ceil : {value_7}")

# from math import * # modül ismi kullanmamıza gerek yok.   *: tümünü dahil et 

# val = factorial(4)
# print(f"factorial value : {val}")
# val_2 = sqrt(9)
# print(f"sqrt value :  {val_2}")

from math import factorial, sqrt, ceil, floor, pow

def abs(x): # en son tanımlanan fonksiyon geçerlidir
    print("Local abs function.")
    if x < 0:
        return -1 * x
    else : return x

v1 = factorial(6)
print(v1)
v2 = sqrt(25)
print(v2)
v3 = abs(-5)
print(v3)