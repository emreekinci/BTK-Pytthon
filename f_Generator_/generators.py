# Bellekte yer isgal etmeyen bir iterator uretir.
# def cube():
#     res  = []
    
#     for i in range(6): # range(100000) icin bellekte cok yer kaplar.
#         res.append(i**3)
#     return res

# print(cube())

def cube():
    for i in range(10):
        yield i**3 # yield sadece iterable bir objedir bellekte yer etmez

# generator = cube() #--> Buna ihtiyac yok bize direkt nesne donuyor
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#iterator = cube() # yield(generator) zaten bize iterable nesneyi çeviriyor 
#1
# for i in iterator:
#     print(i)
#2
for i in cube(): # for kullandigimiz icin StopIteration a kadar devam eder.
    print(i)
    
# yield ile dongu icinde olusan her nesne-obje yeni bir listeye ekleme, esitleme islemlerine gerek kalmadan direkt yazdirilir.
# generator ile yapilan her islem sonucu yield objesiyle bellekte tutulmadan gonderilir 
# cube() uzerinde dolasip her bir elemani almak istedigimizde 


liste = [i**3 for i in range(5)]
print(liste)
generator = (i**3 for i in range(6)) # comprehensive generator
print(generator)

for i in generator:
    print(i)