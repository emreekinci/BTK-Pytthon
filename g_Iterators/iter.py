# liste = [1,2,3,4]

# for i in liste:
#     print(i)
    
# #print(dir(liste))

# list = [1,2,3,4]
# iterator = iter(list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #print(next(iterator)) # StopIteration

# iterator = iter(list)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNums:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start+=1
            return x
        
        else:
            raise StopIteration

# 1- for        
# liste2 = MyNums(10,20)

# for x in liste2:
#     print(x)

# 2- print(next(iter))  xx
liste2 = MyNums(10,20)
myiter = iter(liste2)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# while
while True:
    try:
        element = next(myiter) 
        print(element)
    except StopIteration:
        break 
