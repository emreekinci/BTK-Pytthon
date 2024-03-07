# OOP

# class => Person(name, surname, birthday, calculatAge())

class Person:
    pass # bos class tanımı

    # attributes : class attributes ve object attributes -> constructor
    address = "Space"
    
    # class attributes 
    
    
    # constructor ( yapıcı metod )
    def __init__(self, name, year):
        
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı")
    
        # methods
    

    # lst1 = [1, 2, 3]
    # lst2 = [4, 6, 8]

    # #result = type(lst1)
    # print(type(lst1), type(lst2))

# instance(object)
p1 = Person('Emre', 1999)
p2 = Person('Serdar', 1978)
p3 = Person('Kaan', 2001)

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

print(type(p1))
print(type(p2))
