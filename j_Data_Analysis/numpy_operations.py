import numpy as np

numbers1 = np.random.randint(10,100,6) #Generate 6 random integers between 10 and 100 (inclusive).
print("Numbers1: ", numbers1)
print("Numbers1: ", numbers1+10)

numbers2 = np.random.randint(10,100,6)  #Create a second set of random integers.
print("Numbers2: ", numbers2)
print("Numbers2: ", numbers2+10)


result = numbers1 +  numbers2   #Add the two arrays together element
print( "\nResult: \n", result)       #Print out the results.
result2 = numbers1 -  numbers2        #Subtract one array from another.
print( "Difference:\n", result2)          #Print out the difference.

result3 =  np.multiply(numbers1, numbers2)    #Multiplies each element in 'numbers1' by the corresponding element in 'numbers 
print(result3)  
result4 =  np.dot(numbers1, numbers2)    #Take the dot product of the two arrays.
print("\nDot Product:\n", result4)         #Print out the dot product.

#Find the index of the maximum value in an array.
# max_index = np.argmax(numbers1)
# print("\nIndex of Max Value in Numbers1: %d"% max_index)

#Use this to find the actual maximum value itself.
# max_value = np.amax(numbers1)
# print(max_value)
# sinus = np.sin(numbers1)
# cosinus = np.cos(numbers1)
# sqrt =np.sqrt(numbers1)
# logarithm= np.log(numbers1)
# exp= np.exp(numbers1)

# print ("\nsinus values are :")
# print( sinus)
# print ("\nCosinus values are : ")
# print( cosinus) 
# print ("Square root values are :")
# print( sqrt)
# print ("Logarithmic values are :")
# print( logarithm)
# print ("Exponential values are :")
# print( exp)

mat_num1 = numbers1.reshape(2,3)
mat_num2 = numbers2.reshape(2,3)
res1 = np.vstack((mat_num1,mat_num2))# vertical  stacking of matrices
# print(res1)
res2 = np.hstack((mat_num1,mat_num2))# horizontal stacking of matrices
# print(res2)

isBigger = numbers1 <=60
# print(isBigger)

print(numbers1)
even = numbers1 % 2 == 0
print("\nEven numbers in first column \n", even)
print(numbers1[even])

oddNums = numbers1[~even]
print("\nOdd numbers in first column \n ", oddNums)