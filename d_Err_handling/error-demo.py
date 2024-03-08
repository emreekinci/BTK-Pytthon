liste = ["1","2","3","z6z","1asd","256","aaa","63","12"]

# 1: liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanıcı 'q' değerini girmedikce aldiginiz her inputun sayısal olduğundan emin olunuz aksi halde hata mesajı yaz

# while True:
#     sayi = input('sayi: ')
#     if sayi == 'q':
#         break
#     try:
#         result = float(sayi)
#         print(f"Girilen sayi: {result}")
#         break
#     except ValueError as ve:
#         print(f'Gecersiz sayi girisi --> {ve} ')        
#         continue

# 3: Girilen parola icindeki turkce karakter hatasi veriniz.

# def checkPassord(parola):
    
#     turkish_character = 'çğıöşüİ'

#     for i in parola:
#         if i in turkish_character:
#             raise TypeError("Parola Türkçe karakter içeremez !!")
#         else:   pass
#     print(f"Geçerli parolanız: {parola}")    

# while True:
#     parola = input("Parola : ")
#     try:
#         checkPassord(parola)
#         break
#     except TypeError as er:
#         print(f"Hata: {er}")
#         #continue
        
# 4: Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer icin hata mesajlari versin

def factoriel(x):
    x = int(x)
    
    if x < 0:
        raise ValueError("Sayi degerimiz negatif olamaz !!")    
    
    result = 1
    for i in range(1, x):
        result*=i
    
    return result

for x in [5,15,25,-1,'1aa0']:
    try:
        y = factoriel(x)
    except ValueError as ve:
        print(ve)
        continue
    print(f"x: {x} --> y =  factoriel({x}) = {y}")
        
    