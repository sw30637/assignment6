"""
Sarah Welt
Assignment 6
This Program uses numpy to create and manipulate arrays
"""
import numpy as np  

#Module that creates a 2-D array (without typing it explicitly)
array = np.arange(1,16).reshape(3,5).T 	
print array

#Generates a new array containing the 2nd and 4th rows
print array[[1,3],:]

#Generates a new array that contains the 2nd column
print array[:,1]

#Generates a new array that contains all the elements in the rectangular section between the coordinates [1,0] and [3,2]
print array[1:3,0:2]

#Generates a new array that contains only elements with values that are between 3 and 11
new_array =[]
for i in range (5):
	for j in range (3):
		if array[i,j]>3 and array[i,j]<11:
			new_array.append(array[i,j])
print new_array

#Module that, given the array: 
a=np.arange(25).reshape(5,5) 
#divides each column element-wise with the array
b=np.array([1., 5, 10, 15, 20])

array_divided=(a.T/b).T
print array_divided

#Module that generates a 10X3 array of random numbers in the range[0,1]
random_array =np.random.rand(10,3)

#Picks the number closest to 0.5 for each row
closest = []
for i in range(10):
	random_array_elem= abs(random_array[i,:]-0.5)
	arg= np.argsort(random_array_elem)
	closest.append(random_array[i,arg[0]])

#Uses abs and argsort to find the column for each of the numbers closest to 0.5
for i in range(10):
	random_array_elem= abs(random_array[i,:]-0.5)
	arg= np.argsort(random_array_elem)

#Uses fancy indexing to extract the numbers into an array
number_closest = []
for i in range(10):
	random_array_elem= abs(random_array[i,:]-0.5)
	arg= np.argsort(random_array_elem)
	number_closest.append(random_array[i,arg[0]])

array_closest=np.array(number_closest)
print array_closest

#Module that computes the Mandelbrot fractal using the Mandelbrot iteration



import matplotlib.pyplot as plt 
plt.imshow(mask.T, extent= [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')