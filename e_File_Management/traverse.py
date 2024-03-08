
with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r") as file:
    content = file.readlines()
    for i in content:
        print(i)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2, end="")


# file = open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/file_traverse.txt","r",encoding="utf-8",errors='ignore') 

# content = file.read()
# print(content)
# print(file.tell()) # .tell : cursor location
