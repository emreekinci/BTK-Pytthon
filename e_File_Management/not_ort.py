def not_hesapla(satir):
    satir = satir[:-1] # satırlar arasi bosluklar gitti
    liste = satir.split(':')
    
    ogr_name = liste[0]
    notlar = liste[1].split(',')
    #print(liste)
    #print(notlar)
    #print(notlar[0]+ " "+notlar[1]+" "+notlar[2] )
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    avg = (not1+not2+not3) / 3 
    
    if avg>=90 and avg<=100:
        harf = "AA"
    elif avg>=85 and avg<=89:
        harf = "BA"
    elif avg>=75 and avg<= 84:
        harf = "BB"
    elif avg>=70 and avg<= 74:
        harf = "CB"
    elif avg>=65 and avg<= 69:
        harf = "DC"
    elif avg>=60 and avg<= 64:
        harf = "DD"
    elif avg>=50 and avg<= 59:
        harf = "FD"
    else:
        harf = "FF"
        
    return ogr_name+ ": " + harf+ "\n"
    
def not_gir(): # not girisi yapilan yer
    ad = input('Name: ') # format-->  name surname: xxx, xxx, xxx
    soyad = input('Surname: ')
    not1 = input('Note1: ')
    not2 = input('Note2: ')
    not3 = input('Note3: ')
    
    with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/notlar.txt","a") as file:# w: her eklemede dosyayi siler.  --> a ekleme yapmak icin
        file.write(ad +' '+soyad+': '+not1+','+not2+','+not3+'\n')

def ortalamalari_oku():
    with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/notlar.txt","r") as file: # r: okuma-read islemi
        for satir in file:
            print(not_hesapla(satir))
            #satir.split[]
            
def notlari_kaydet():
    with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/notlar.txt","r") as file: # r: once okuma yap
        liste= [] # bos liste
        
        for i in file:
            #print(i)
            liste.append(not_hesapla(i)) # her satiri(name: not1, not2, not3) listeye not_hesapla() dan donen degeriyle aldik
            
            with open("C:/w_emre_desktop/Roof/BTK/Python/File_Management/sonuclar.txt","w") as file2: # w: sonuclar.txt yoksa oluşturacak
                for i in liste:
                    file2.write(i)     # sonuclari sonuclar.txt ye yazdik             

while True:
    islem = int(input('Yapabileceğiniz Islemler:\n1-Notları Oku\n2-Not Gir\n3-Notları Kaydet\n4-Çıkış\n'))
    
    if islem == 1:
        ortalamalari_oku()
    elif islem == 2:
        not_gir()
    elif islem == 3:
        notlari_kaydet()
    else:
        break
    
    