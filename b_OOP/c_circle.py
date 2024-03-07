import math

class circle:
    # class object attribute
    pi = 3.14
    
    def __init__(self,  r=1):
        self.r = r
        
    # methods
    def cevreHesapla(self):
        return 2  *  self.pi  * self.r
        
    def alanHesapla(self):
        return self.pi  * (pow(self.r, 2))
    
c1 = circle() # default : r = 1
c2 = circle(6)

print(f"c1: alan ={c1.alanHesapla()} ve cevre={c1.cevreHesapla()}")
print(f"c2: alan ={c2.alanHesapla()} ve cevre={c2.cevreHesapla()}")