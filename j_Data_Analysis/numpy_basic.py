import numpy as np

# python list -> Basit islemler icin
# py_list = [1,2,3,4,5,6,7,8,9]

# numpy array 
# np_array = np.array([1,2,3,4,5,6,7,8,9])
# print(type(py_list))
# print(type(np_array))

# py_multi = [[1,2,3],[4,5,6],[7,8,9]]
# np_multi = np_array.reshape(3,3)

# print(py_multi)
# print(np_array.ndim)
# print(np_array.shape)

# print(np_multi)
# print(np_multi.ndim)
# print(np_multi.shape)

# print("---------- PART2 ---------------")
# res = np.array([2,9,8,45,25,22,10])
# print(res)
# res2 = np.arange(1,11) 
# print(res2)
# res3 = np.arange(1,11,2) 
# print(res3)
# res4 = np.zeros(10)
# print(res4)
# res5 = np.ones(12)
# print(res5)
# res6 = np.linspace(0,100,5)
# print(res6)
# res6_2 = np.linspace(0,5,5)
# print(res6_2)
# res6 = np.random.randint(0,10)
# print(res6)
# res7 = np.random.randint(20)
# print(res7)
# res8 = np.random.randint(2,25,4)
# print(res8)
# res9 = np.random.rand(5) 
# print(res9)
# res10 = np.random.randn(5)
# print(f"{res10}\n******************")
# np_arr = np.arange(50)
# np_dimens = np_arr.reshape(10,5) # 10 satır, 5 sütun
# print(np_dimens)
# print(np_dimens.sum(axis=0))#sütunlardaki toplamlar-> 5 tane 
# print(np_dimens.sum(axis=1))#satırlardaki toplamlar-> 10 tane

# nums = np.random.randint(1,100,10)
# max = nums.max()
# min = nums.min()
# mean = nums.mean()
# maksindex = nums.argmax()
# minindex = nums.argmin()
# print(nums, max, min, mean, maksindex, minindex)

print("---------- PART3 ---------------")
numbers = np.array([0,5,10,15,20,25,30,40,50,60])
res = numbers[5] # 5. index
print(res)
res2 = numbers[-1] # son eleman
print(res2)
res3 = numbers[0:3] # 3e kadar
print(res3)
res4 = numbers[:3] # 3 e kadar
print(res4)
res5 = numbers[3:] # 3 den sona kadar
print(res5)
res6 = numbers[::] # hepsi
print(res6)
res7 = numbers[::-1] #  sağdan sola hepsi
print(res7)
print("-----------------")
numbers_2 = np.array([[0,5,10],[15,20,25],[30,40,50],[60,70,80]]) # 4*3
print(numbers_2)
result = numbers_2[0]
print(result)
result2 = numbers_2[2]
print(result2)
result3 = numbers_2[0,2]
print(result3)
result4 = numbers_2[3,2]
print(result4)
result5 = numbers_2[::-1]
print(result5)
result6 = numbers_2[:,2] # her satırın 3. elemanını getir
print(result6)
result7 = numbers_2[:,0:2] # tüm satırları seç ve her satırdan 0 ve 2. index arasını al
print(result7)
result8 = numbers_2[:,1:3]
print(result8)
result9 = numbers_2[-1,:] # son satırı al
print(result9) 
result10 = numbers_2[:2,:3] # ilk iki satırı  ve ilk üç sütunu al 
print(result10) 
print("------referans--------")
arr1 = np.arange(0,10)
arr2 = arr1 # referans
print(arr1)
print(arr2)
arr2[0]  = 20
print(arr1)
print(arr2)
# arr1 değişti mi? evet..
print("-------view--------")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 0
print(arr) # [0 2 3 4 5]
print(x)   # [0 2 3 4 5]
print("-------view--------")
array2 = np.array([1, 2, 3, 4, 5])
x2 = array2.view()
x2[0] = 10
array2[1] = 20
print(array2.base is x2.base) # False
print(array2.base is array2)    # False
print(x2.base is x)        # False
print(array2[0])             # 10
print(x2[0])              # 10
print(array2[0])
print(x2[1])
print("-------copy----------")
arr3 = np.array([1, 2, 3, 4, 5])
x3 = arr3.copy()
arr3[0] = 0
print(arr3) # [0 2 3 4 5]
print(x3)   # [1 2 3 4 5]





# Sources: discuss.python.org (1) ahmetardahanli.com (2) kerteriz.net (3) geeksforgeeks.org (4)

# NumPy dizilerinde, view() metodu, orjinal diziyi görüntülemek için kullanılabilir. Ancak, orjinal dizinin değerlerine doğrudan erişim sağlar ve değişiklikleri orjinal dizide yansıtır. Bu nedenle, aşağıdaki kod parçacığında, arr dizisinin değerleri değişir:

# python
# Copy code
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 0
# print(arr) # [0 2 3 4 5]
# print(x)   # [0 2 3 4 5]
# Bu davranışı önlemek için, copy() metodunu kullanarak diziyi kopyalayabilirsiniz:

# python
# Copy code
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 0
# print(arr) # [0 2 3 4 5]
# print(x)   # [1 2 3 4 5]
# Yeni bir görünüm oluşturmak istediğinizde, view() metodunu kullanabilirsiniz, ancak bu durumda, değişiklikler orjinal dizide yansıtılır. Örneğin:

# python
# Copy code
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 10
# print(arr) # [10 2 3 4 5]
# print(x)   # [10 2 3 4 5]
# Bu durumda, x dizisi arr dizisinin görünümüdür ve değişiklikleri arr dizisinde de yansıtılır. Ancak, x dizisinde yapılan değişiklikler x dizisinde saklanır. Örneğin:

# python
# Copy code
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 10
# print(arr.base is x.base) # True
# print(arr.base is arr)    # True
# print(x.base is x)        # True
# print(arr[0])             # 10
# print(x[0])              # 10
# Yukarıdaki örnekte, arr ve x dizilerinin aynı göstericiyi paylaşır ve base özelliği, orjinal diziye işaret eder. Bu nedenle, arr ve x dizilerinin değerleri aynıdır ve her iki dizide de değişiklikler yansıtılır. Ancak, x dizisinde yapılan değişiklikler sadece x dizisinde saklanır.

# Ayrıca, view() metodunu kullanarak bir dizinin görünümünü alabilirsiniz, ancak bu durumda, orjinal dizinin değerlerine doğrudan erişim sağlayacaktır. Örneğin:

# python
# Copy code
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# print(x.base is arr) # True
# print(x.base is x)   # True
# print(x[0])          # 1
# print(arr[0])       # 1
# Bu durumda, x dizisi arr dizisinin görünümüdür ve orjinal dizinin değerlerine doğrudan eri