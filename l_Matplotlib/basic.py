import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# example1
# x = [12,34,56,78]
# y = ['A','B','C','D']

# fig=plt.figure()
# ax1=fig.add_subplot(111) # create an axes in  the figure at position (1,1)
# ax1.bar(x, y)         # plot a bar chart using x and y data
# plt.show(block=False)   # display the plot on screen

# example 2 - stacked bars 
# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x, y, "o--r")  # -g, --g, -b, ...  --> o:marker, --:type of line, r:red
# plt.axis([0,6,0,20]) # (x_min, x_max, y_min, ymax)

# plt.title("Grafik Başlığı")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()

# example3
# x = np.linspace(0,3,100)

# plt.plot(x, x, label="linear",color="red")
# plt.plot(x, x**2, label="quadratic",color="blue")
# plt.plot(x, x**3, label="cubic",color="green")

# plt.xlabel("x label: x")
# plt.ylabel("y abel: x^2")

# plt.title("simple plot")
# plt.legend()
# plt.show()

# example4 
# x = np.linspace(0,2,100)
# fig, axs = plt.subplots(3)
# axs[0].plot(x, x, color="red")
# axs[0].set_title("linear")

# axs[1].plot(x, x**2, color="blue")
# axs[1].set_title("quadratic")

# axs[2].plot(x, x**2, color="blue")
# axs[2].set_title("cubic")

# plt.tight_layout()
# plt.show()

# example5
# x = np.linspace(0,2,100)
# fig, axs = plt.subplots(2,2)
# fig.suptitle("grafik başlığı")

# axs[0, 0].plot(x, x, color="red")
# axs[0, 1].plot(x, x**2, color="blue")
# axs[1, 0].plot(x, x**3, color="grey")
# axs[1, 1].plot(x, x**4, color="black")

# plt.show()

# example6

df = pd.read_csv("C:/w_emre_desktop/Roof/BTK/Python/k_Pandas/nba.csv")
# print(df.head())

# not dropping row:   "age","PER","BPM"
df = df.drop(["Rk","Unnamed: 19","Unnamed: 24","Player","Pos","G","MP","TS%","3PAr","FTr","ORB%","DRB%","TRB%","AST%","STL%","BLK%","TOV%","USG%","OWS","DWS","WS","WS/48","OBPM","DBPM","VORP"], axis=1).groupby("Tm").mean() # ,"Pos","G","MP","PER","TS%","3PAr","FTr","ORB%","DRB%","TRB%","AST%","STL%","BLK%","TOV%","USG%","OWS","DWS","WS","WS/48","OBPM","DBPM","BPM","VORP"
df.head().plot(subplots=True)
# plt.xlabel("Team") # Tm
# plt.ylabel("Age mean: for every Team") # age mean for all od

plt.legend()
plt.show()
# for matplotlib library --> pip install matplotlib