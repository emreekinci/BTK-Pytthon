# Dosya aç - oluştur: open()
# Kullanımı: open(file_name, erişim_modu)
# erişim modu: dosyayı hangi amaçla açtığımızı belirtir.

# "w": (write) yazma modu. Dosyayı konumda oluşturur.
#       Dosya içeriğini siler ve yeniden ekleme yapar   
 
# file = open("newFile.txt", "w") # <_io.TextIOWrapper name='newFile.txt' mode='w' encoding='cp1254'>
# file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","w")

# file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","w",encoding='utf-8')
# #file.write("Emre Ekinci")
# file.write("Ben Emre Ekinci, Veri Bilimi ve Veri Analistliği ile ilgileniyorum.. ")
# file.close()

# file.close()

# "a": (append) ekleme. Dosya konumda yoksa oluşturulur.

# file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","a",encoding='utf-8') # a: dosyanın son kısmından ekleme yapar.
# file.write("\nDurmadan ilerleyeceğim..")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir. 

#file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file2.txt","x",encoding='utf-8') # ikinci çalışmada hata verir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir
# file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","r",encoding="utf-8")
# for i in file:
#     print(i)
# olmayan dosyayı okuma işlemi:
# try:
#     file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file3.txt","r",encoding="utf-8")
#     for i in file:
#         print(i)
        
# except FileNotFoundError:
#     print("Dosya okunamadı.")
# finally:
#     print("Dosya kapandı.")

file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","r",encoding="utf-8")
# for i in file:
#     print(i, end=" ")


# ------------ READ
# content = file.read()
# print("içerik 1")
# print(content) # cursor dosyanın en sonunda

file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/new_file.txt","r",encoding="utf-8") # içeriği tekrar okur
# content2 = file.read()
# print("içerik2")
# print(content2)
# file.close() # boşluk

# content = file.read(15)
# content = file.read(20)
# content = file.read(20)
# content = file.read(20)

# print(content)
# file.close()

# ------------- READLINE

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline())
# print(file.readline())

# ------------ READLINES

liste = file.readlines() 
for eleman in liste:
    print(eleman,end="")

file.close()
