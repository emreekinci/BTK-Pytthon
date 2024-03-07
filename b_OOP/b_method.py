# OOP

# class => Person(name, surname, birthday, calculatAge())

class Person:
    pass # bos class tanımı

    # attributes : class attributes ve object attributes -> constructor
    address = "Space"
    
    # class attributes 
    
    
    # constructor ( yapıcı metod )
    def __init__(self, name, year, age):
        
        # object attributes
        self.name = name
        self.year = year
        self.age = age
        print("init metodu çalıştı")
    
    # instance methods **
    def intro(self):
        print(f"Hello There. I'm {self.name} and my birthyear's: {self.year}")
    
    def calculateAge(self):
        return 2024 - self.year

# instance(object)
p1 = Person('Emre', 1999, 'Çanakkale')
p2 = Person('Serdar', 1978, 'İzmir')
p3 = Person('Kaan', 2001, 'Yalova')

# updating
p2.name = "Sezgin Ahmet"
p2.year = 1988
p3.name = "Kaan Dursun"
p3.year  = 2002 
p3.address = "Bursa"

# accessing object attributes
print(f"\nname: {p1.name} year: {p1.year} address: {"İstanbul"}")
print(f"name: {p2.name} year: {p2.year} address: {"Ankara"}")
print(f"name: {p3.name} year: {p1.year} address: {p3.address}\n")

p1.intro()
p2.intro()

print(f"\nname : {p1.name} and age: {p1.calculateAge()}")
print(f"name : {p2.name} and age: {p2.calculateAge()}")

p2.calculateAge()