import random
from random import shuffle

# terminal bash --> py _random.py ile çalıştır 
# res = dir(random) 
# res2 = help(random)

# print(res)
# print(res2)

result_ran = random.random() # 0.0 - 1.0
result_ran2 = random.random() * 100
result_ran3 = int(random.uniform(1, 10))
result_ran4 = random.randint(1, 100)  # ***

name_val = ['Emre', 'Murat', 'Sergen', 'Tahir','Basri'] 
res_name = name_val[random.randint(0, len(name_val)-1)]
res_name2 = random.choice(name_val)

liste = list(range(10))
res_l = liste.copy()
shuffle(res_l) # from random import --> shuffle olmasa random.shuffle(liste)
res_l.append(12) 

res_sample = random.sample(liste, 3)
res_sample_name = random.sample(name_val, 2) 
print(result_ran)
print(result_ran2)
print(result_ran3)
print(result_ran4)

print(res_name)
print(res_name2)

print(f"\nfirst : {liste}")
print(f"with shuffle: {res_l}")
print(f"with sample: {res_sample}")
