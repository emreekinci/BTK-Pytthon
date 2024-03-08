import json
import os

class Users:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class userRepository:
    def __init__(self):
        self.users = [] ## uygulama basinda bos liste
        self.isLoggedIn = False
        self.currentUser = {} #user nesnesi tutacak ve isLoggedIn true olduğunda user bilgileri gelecek
        
        # load users from .json file
        self.loadUsers() # userRepository oluşturulduğu anda çağırıyoruz
    def loadUsers(self): # file reading
        if os.path.exists('demo.json'):
            with open('demo.json', 'r') as f:
                users = json.load(f)
                print(users)
                for usr in users:
                    #print(usr)
                    #print(usr['username']) # not python object
                    usr = json.loads(usr)
                    #print(usr['username']) #python object
                    newUser = Users(username= usr['username'], password=usr['password'], email=usr['email'])
                    self.users.append(newUser) # newUser.__dict__
            print(self.users)
        
    def register(self, user: Users):  # create user
        self.users.append(user)
        self.savetoFile() # yeni kayıtlı userların dosyaya kaydedilmesini sağlıyoruz
        print("Users created..")
        
    def login(self, username, password):
        if self.isLoggedIn:
            print('You are already login !!')
        else:
            for user in self.users:
                if user.username == username and user.password == password: 
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Login Successful! Welcome ", username)
                    break
        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Exit succesfully")
        
    def identity(self):
        if self.isLoggedIn:
            print(f"You are {self.currentUser.username}")
        else: 
            print("No Login ...")  
    
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('demo.json', 'w') as f:
            #json.dump([usr.__dict__ for usr in self.users],f) # objeyi direkt yazamayız o yüzden dicte cevirdik
            json.dump(list,f)
            
repository = userRepository()   # disarda tanimli çünkü içerde sürekli set edilir ve sıfırlanır..
    
while True:
    print("  Menü: ".center(50, '='))
    choose = input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeçiminiz:') 
    if choose == 5 :
        break
    else:
        if choose == '1': # Register
            username = input('username: ')
            password = input('Password: ')
            email = input('email: ')
            
            user = Users(username=username, password=password, email=email)
            repository.register(user)
            print(repository.users)
            
        elif choose == '2': # Login
            if repository.isLoggedIn:
                print("you are already logged in")
            else:
                username = input('username: ')
                password = input('password: ')
                #email = input('email: ')
                repository.login(username, password)
            
        elif choose == '3': # Logout
            repository.logout()
            
        elif choose == '4': # identity  
            repository.identity()
        elif choose == '5': # Exit
            break
        else:
            print("False chosen is done !!")
            continue