# r+ : okuma ve güncelleme modu 

# with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r+") as file:
#     file.write("Hey ben")
    
# with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r+") as file:
#     print(file.read())

# ----------  SAYFA SONU GÜNCELLEME
# with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","a",encoding="utf-8") as file:
#     file.write("\na modu ile eklenen kelimelerim...")
    
# ----------  SAYFA BASINDA GÜNCELLEME
# with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r+") as file:
#     content = file.read()
#     content = "Sayfa basinda guncelleme yazim.\n" + content
#     #print(content)
#     file.seek(0)
#     file.write(content)
    
# with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r") as file:
#     print(file.read())

with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r+") as file:
    list = file.readlines()
    list.insert(2,"Sayfa ortasina insert ile guncelleme3.\n")
    #print(list)
    file.seek(0)
    file.writelines(list)
    # for i in list:
    #     file.write(i)
        
with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r") as file:
    print(file.read())     