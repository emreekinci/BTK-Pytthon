import matplotlib.pyplot as plt

"""
yıl = [2019,2020,2021,2022,2023,2024]

oyuncu1 = [46,59,62,49,54,50] 
oyuncu2 = [59,52,46,38,36,37]
oyuncu3 = [37,38,53,49,42,39]

# stack plot
plt.plot([],[],color="y",label='Oyuncu 1')
plt.plot([],[],color="r",label='Oyuncu 2')
plt.plot([],[],color="b",label='Oyuncu 3')

plt.stackplot(yıl, oyuncu1, oyuncu2, oyuncu3, colors= ['yellow', 'red','blue'])
plt.legend()
plt.xlabel('Yıllar')
plt.ylabel('Skor')
plt.title("Çoklu Oyunculara Ait Skorlar")
plt.show()
"""

"""
# pie grafiği
goal_types = 'Penaltı',"Kaleye Atılan Şut", "Serbest Vuruş"

goals = [22,35,50] 
colors = ['y', 'r', 'b']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True, explode=(0.05,0.05,0.05),autopct="%1.1f%%")
plt.show()
"""

"""
# bar
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,30,50,60],label="Audi",width=.5)

plt.legend("Gün")
plt.xlabel("Mesafe (km)")
plt.ylabel("Araç Bilgileri")

plt.show()
"""

"""
#Histogram Grafiği

yaslar = [22,55,45,12,15,66,88,49,26,24,20,35,77,88,16,22,66,55,99,42,28,8,12,42,58,54,99,6,68]
yas_gruplar = [0,10,20,30,40,50,60,70,80,90,100] #  yas aralıkları

plt.hist(yaslar,yas_gruplar,histtype="bar",rwidth=0.8)
plt.title("Histogram Graph")
plt.xlabel("Yas Grupları")
plt.ylabel("Kişi Sayısı-Frekans")
# plt.ylabel(r"$\mathregular{Frequency}$")
plt.xticks(yas_gruplar)
plt.grid(axis='both') 

plt.show()
"""