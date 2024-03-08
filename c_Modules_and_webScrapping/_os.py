import os
import datetime

# res = dir(os) # definiton embedded objects and funtions...
#res = os.name # win-mac... nt: windows

# change directory(folder)
#os.chdir('C:\w_emre_desktop\Roof\BTK\Python\os_directory') # os.chdir('C:\\') different place with path
#os.chdir('../..')

# create, remove, rename folder
#os.mkdir("os_directory") # new folder same path
#os.makedirs("os_directory/newFolder")
#os.rename("os_directory","os_Directory_rnm")
#os.rmdir("os_Directory_rnm/asdsadas")  # asdsadas


# active directory
res_directory = os.getcwd() # available file location

# listing
#res = os.listdir()
#res = os.listdir("C:\\")
# for folder in os.listdir(): # filtering
#     if folder.endswith('s'):
#         print(folder)

# info = os.stat("d_Err_handling\\error-demo.py") #os.stat_result(st_mode=33206, st_ino=6473924464452106, st_dev=8407920967626476262, st_nlink=1, st_uid=0, st_gid=0, st_size=1758, st_atime=1709374411, st_mtime=1709031999, st_ctime=1709028332)
# print(info)

# date deails
#res = os.stat("d_Err_handling\\errors.py")
#res = res.st_size/1024
#res = datetime.datetime.fromtimestamp(res.st_ctime) # 2024-02-27 02:11:05.620497 -> creation date
# res = datetime.datetime.fromtimestamp(res.st_atime) # acces date
# res = datetime.datetime.fromtimestamp(res.st_mtime) # modified date

# run notepad
#os.system("notepad.exe")

# path
res = os.path.abspath("_os.py")
res = os.path.dirname("C:/w_emre_desktop/Roof/BTK/Python/c_Modules/_os.py")
res = os.path.dirname(os.path.abspath("_os.py"))
res = os.path.exists("C:/w_emre_desktop/Roof/BTK/Python/c_Modules/_os.py") # is there _os.py--> ("o")
#res = os.path.exists("C:/w_emre_desktop/Roof/BTK/Python/c_Modules/_os2.py") # is there _os2.py--> ("o")

res1 = os.path.isfile("C:/w_emre_desktop/Roof/BTK/Python/c_Modules/_os.py") # is this a folder
res2 = os.path.isdir("C:/w_emre_desktop/Roof/BTK/Python/c_Modules") # is this a file
res3 = os.path.join("c:\\","deneme","deneme2")
res4 = os.path.split("C:/w_emre_desktop/Roof/BTK/Python/c_Modules")
res5 = os.path.splitext("_os.py")
spltxt = res5[0]
spltxt2 = res5[1]
print(res_directory,res1,res2,res3,res4,res5,spltxt,spltxt2)


