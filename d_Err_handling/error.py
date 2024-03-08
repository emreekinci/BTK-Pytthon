from math import floor
# error => hata


# print(a) # NameError
# int('asdad25') # ValueError
# print(10/0) # ZeroDivisionError
# print('deneme'sad) # SyntaxError


# error handling

# try: 
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(floor(x/y))
#     print(float(x/y))
# except:
#     print('Yanlış bilgi girişi !!')
# else:
#     print('Her şey yolunda..')
# except ZeroDivisionError:
#     print('y için 0 değeri girilemez !!')
# except ValueError:
#     print('x ve y için sayısal değerler girilmeli !!')

# except (ZeroDivisionError,ValueError) as err:
#     print('Hatalı bilgi girişi !!')
#     print(err)
# while True:
#     try: 
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(floor(x/y))
#         print(float(x/y))
#     except:
#         print('Yanlış bilgi girişi !!')
#     else:
#         print('Kullanıcı isteneni yapana kadar döngü başa döndü ve uygun değerleri girince kırıldı.')
#         break

while True:
    try: 
        x = int(input('x: '))
        y = int(input('y: '))
        print(floor(x/y))
        print(float(x/y))
    except Exception as exc: # error base of name is Exception 
        print('Yanlış bilgi girişi !! =>>', exc)
    else:
        print('Kullanıcı isteneni yapana kadar döngü başa döndü ve uygun değerleri girince kırıldı.')
        break
    finally: # mesela dosya açtık işlemler bitince daima dosyayı kapatma işlemleri için vb.
        print('Her zaman çalışır burası...')

 