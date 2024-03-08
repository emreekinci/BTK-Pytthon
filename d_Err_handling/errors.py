# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakter olmalidir.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola kücük harf icermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf icermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola icerisinde en az bir rakam olmalidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("alpha numeric karakterlerden : £#$ icermelidir.")
#     elif re.search('\s', psw):
#         raise Exception("Parola bosluk karkateri içermemelidir.")
#     else:
#         print("Parola uygundur...")
    
# password = "1357925Aa_"

# try:
#     check_password(password)
# except Exception as ex:
#     #print("*************************************")
#     print(ex)
# else:
#     print("Parola uygundur: else ")
# finally:
#     print("Validation tamamlandı.......")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Fazla karakter name alanında !!")
        else:
            self.name = name
            
p = Person("xxxxEmreeeee", 1999)