def greeting(name):
    print('Hi,',name)
    
# print(greeting("Emre"))
# print(greeting)

# sayHi = greeting # adresler tutulur
# print(greeting)
# print(sayHi)

# del sayHi
# print(greeting)

# encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         num1+=1
#         return num1
#     num2 = inner_increment(num1)
#     print(num1, num2)
    
# outer(10)
#inner_increment(20)

def fact(number):
    if not isinstance(number, int):
        raise TypeError("Number value must be an integer")
    
    if not number >= 0:
        raise ValueError("Number value must be zero or positive")
    
    def inner_fact(number):
        if number <= 1:
            return 1
        return number * inner_fact(number-1) 
    return inner_fact(number)

def until_inp(istenen): # ekle: 
    if istenen >=0:
        for i in range(1, istenen+1):
            print(f"fact({i}): {fact(i)}")      
    # else:
    #     fact(istenen)
                

while True:           
    try:
        fact_range = int(input("Expecting fact range is: "))
        until_inp(fact_range)
        # if not isinstance(fact_range, int):
        #     raise ValueError("False input entrance !")
    except ValueError as ve:
        print("False input entrance !! --> ",ve)
        print("Do u wanna exit ?(y/n)")
        #res = input("(y/n)\n:"
        res = input("(y/n)\n:")   
        if res == 'y' :
            break
        #if not res == 'n':
            # while res != 'n' and res !=y:
            #     res = input("For continue: press 'n'\n")
        while res != 'n' :  #and res != 'y':
            res = input("For continue: press 'n'\n")
            #res = input("For continue: press 'n'\n")
        # else
            
            
                
        
    # else:
    #     print("For exit: q")
    #     if fact_range == "q":
    #         break
    # finally:
    #     print("En son kısımdayız")
    #     print("For exit: q")
    #     if fact_range == "q":
    #     break
        


    

