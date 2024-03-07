# Inheritance

# Person => name, lastname, age, gender eat(), walk(), sleep(), run(), drink(), fight(), jump()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")
        
    def who_am_i(self):
        print("I'm a Person element.")
        
    def eat(self):
        print("I am eating food\n")
        
class Student(Person):
    def __init__(self, fname, lname, number): # fname, lname Person() parentında var  child class'ta olmalı
        Person.__init__(self, fname, lname) # Person() classındaki eşitlemeler yapılır --> Person.init yerine super().init(fname, lname)
        self.studentNumber = number
        print('Student created')
        
    # overriding    
    def who_am_i(self):
        print('I am a student')
        
    def say_hi(self): # only class Student method
        print('Hi, what a beautiful day\n')  
        
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  
        self.branch = branch     
        
    def who_am_i(self):
        print(f"\nI'm a {self.branch} teacher")   

p1 = Person('Ali','Yalın') 
s1 = Student('Buğra', 'Aydan',1656)
t1 = Teacher('Kenan', 'Sefa', 'Espanol')

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()
p1.eat()
s1.eat()
s1.say_hi()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
