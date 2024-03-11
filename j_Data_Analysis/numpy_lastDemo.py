import numpy as np
 
# 1- (10, 15, 30, 45, 60) değerlerine sahip numpy dizisi oluştur
#my_array = np.array([10])
lastarray = np.arange(15, 70, 15)
lastarray = np.insert(lastarray, 0,10) 
print(lastarray, type(lastarray), "\n") #   output: [10 15 30 45 60] <class 'numpy.ndarray'>

# 2- (5-15) arasındaki sayılarla numpy dizisi olustur
res1 = np.arange(5, 15)
print(res1, "\n") # output: []

# 3- (50-100) arasında 5 er 5 er artarak numpy dizisi olustur
res2 = np.arange(50,100,5)
print(res2, "\n")
# 4- 10 elemanlı sıfırlardan oluşsan dizi
res4 = np.zeros(10)
print(res4, "\n")
# 5- 10 elemanlı birlerden olusan dizi
res5 =  np.ones(10)
print(res5, "\n")
# 6- (0-100) arasında eşit aralıklarla 5 sayı üret
res6 = np.linspace(0,100,5)
print(res6,"\n")
# 7- (10-30) arasında rastgele 5 tane sayı üretin
res7 = np.random.randint(10,30,size=5)
print(res7,"\n")
# 8- (-1,1) arasında 10 adet sayı üret
res8 = np.random.uniform(-1,1, size=10) # randn
res8_1 = np.random.randn(10)
print(res8, res8_1, "\n")
# 9- (3x5) boyutlu (10-50) arasında rastgele bir matris oluşturunuz
res9 =  np.random.randint(10,50,(3,5))
res9_1 = np.random.randint(10,50,15).reshape(3,5)
print(f"with size: 3x5 \n{res9}\nwith reshape: 3x5 \n{res9_1}")
# 10- (5x3) boyutlarında (10-50) arasında üretilen matrisin satır ve sütun toplamlarını yaz
#res10 = np.random.randint(10,50,(5,3))   
rowTotal = res9_1.sum(axis=1) #   summing each row
colTotal = res9_1.sum(axis=0) #   summing each column
print(rowTotal,"\n")
print(colTotal,"\n")
# 11- Üretilen matrisin en büyük en küçük ve ortalaması nedir?
res11 =  res9_1.max()
res11_1 = res9_1.min(axis=None) # axis None means all columns
res11_2 = res9_1.mean(axis=None)
res11_3 = res9_1.ptp(axis=None) # peek to peak
print("Max Value : ", res11, "\n")
print("Min Values : ", res11_1 , "\n")
print("Means : ", res11_2, "\n")
print("Peeks To Peaks : ", res11_3, "\n") #  positive difference between max and min    
# 12- Üretilen matrisin maks ve min değerinin indeksi?
res12 = res9_1.argmax() # maks value index
res12_1 = res9_1.argmin()
print(res9_1)
print(res12,res12_1)
# 13- (10-20) arasındakş sayıları iceren dizinin ilk 3 elemanı
res13 = np.arange(10,20)
res13= res13[:3] #   get the first 3 elements of array
print(res13)
# 14- Üretilen dizinin elemanlarını tersten yazdır
res14 = res9[::-1]
print(f"tersten: \n{res9}\n")
# 15 - üretilen matrisin ilk satırını seç.
first_row = res9[0]
last_row = res9[-1]

print(f"First row: {first_row}\n")
print(f"Last  row: {last_row}\n")
# 16- Üretilen matrisin 2. satır 3. sütunundaki eleman?
res16 = res9[1,2] 
print(f"The element in second row, third column is: {res16}\n")
# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seç
res17 = res9[:,0] # 2. eleman -> res9[:1]
print(f"firs col: {res17}")
res17_2 = res9[:,-1]
print(f"Last col : {res17_2}\n")
# 18- Üretilen matrisin her bir elemanının karesini al
res18 = np.square(res9) 
print(f"Square of every number:\n{res18}\n")

# Asagıdaki ornek için aralığı -50,+50 olan yeni matris tanımlanıp işlem yapmak daha mantıklı üstteki res9 kullanıyoruz
# res9_1 = np.random.randint(-50,50,15).reshape(3,5) yapmak lazım
# 19- Üretilen matris elemanlarının hangisi çift sayıdır? Aralığı (-50,+50) arasında yap
    # the first way for AI
even_numbers = res9[(np.mod(res9,2)==0)&(abs(res9)>=-50)&(abs(res9)<=50)]
odd_numbers = res9[(np.mod(res9,2)!=0)&(abs(res9)>=-50)&(abs(res9)<=50)]
print(f"\nEven numbers are:\n{even_numbers}\n")
print(f"Odd numbers are:\n{odd_numbers}\n")
    # second way for human
print(res9)
res19 = res9 % 2 == 0 # true output --> odd
print(f"------ true false ------\n{res19}")
res19_1 = res9[res19]
print(f"------- odds ------\n{res19_1}")
res19_2 = ~res19_1
print(f"------- evens -----\n{res19_2}")
odds = res9[res9 % 2 == 0]
res_odds_and_positive = odds[odds > 0]
print(f"Odd and positive numbers are:\n{res_odds_and_positive}\n")

# More realistic than the example above :
# res9_1 = np.random.randint(-50,50,15).reshape(3,5) yapmak lazım
matris_2d = np.random.randint(-50,50,30).reshape(5,6)
print(f"2D matrix is: \n{matris_2d}\n")

odds_matris = matris_2d % 2 == 0 
print(odds_matris) # boolean
# odds and positive numbers
odds_val = matris_2d[odds_matris]
print(f"\nodds values : \n{odds_val}")
odds_val_and_positive = odds_val[odds_val > 0]
print(f"\nodd and positif numbers are :\n{odds_val_and_positive}")