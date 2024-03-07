# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasina ulasabilir.".format(role, page)
#         else:
#             return "{0} rolü {1} sayfasina ulasamaz".format(role, page)
#     return inner
        
# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))

# part2
# def islem(islem_adi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam+=i
#         return toplam
    
#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim*=i
#         return carpim
    
#     if islem_adi == 'toplama':
#         return toplam
    
#     else:
#         return carpma 
    
# toplama = islem("toplama")
# print(toplama(1,2,3,4,5,6,7,8,9,10))

# carpma = islem("carpma")
# print(carpma(1,2,3,4,5,6))

# parameters : fonksiyon parametresini göndererek

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == 'toplama':
        print(f1(2,3))
    elif islem_adi == 'cikarma':
        print(f2(5,3)) 
    elif islem_adi == 'carpma':
        print(f3(20,12))
    elif islem_adi == 'bolme':
        print(f4(25,5))
    else:
        print("Gecersiz islem...")
        
islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "toplamaa") # gecersiz kullanim




