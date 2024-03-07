myList = [1,2,3]
# myString = "random string text"

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration) -> None:
        self.title = title
        self.director = director
        self.duration = duration
        print("\nmovie objesi oluşturuldu")
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Obje silindi !!")

m = Movie('film ad', 'yönetmen',138)

# print(type(m))
# print(len(m)) # len metodu yoktu objede sonradan ekliyoruz --> def __len__(self)    ||   def __str__(self)

#print(myList) # str(myList) : aynı sonuc
print(m)      # str(m)
#print(len(m))

del m # m objesini siler  --> def __del__() obje silinmeden kullanıcıya mesaj verir  
#print(m) # NameError: name is not defined
