############################
## Numpyarrays and vectors
############################
##
## Arrays

import numpy as np
arr1 = np.array([1,2,3,4,5]) #1D
print(arr1)
print(arr1.shape)

arr2 = np.array([[1,2,3,4,5]]) #2D : 1 raw, 5 column
print(arr2)
print(arr2.shape)

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2D : 2 raw, 5 column
print(arr2)
print(arr2.shape)
print(arr2[0]) #sor
print(arr2[1][2]) #adott elem
print(arr2[1:,2:]) #adott szeletelés
print(arr2[0:2,3:]) #adott szeletelés
print(arr2>5) #logikai műveletek
print(arr2[arr2>5]) #logikai műveletek

print("--------")
print(np.arange(0,12).reshape(3,4)) #elrendezi adott sor, oszlopba


print(np.ones((3,4))) #feltölti 1-vel
print(np.eye(3)) # diagonál mátrix

## vectorize operation
arr1 = np.array([1,2,3,4,5]) #1D
arr2 = np.array([10,20,30,40,50]) #1D
print(arr1+arr2)
print(arr1*arr2)
##. sqrt, exp, log, egyéb vektor függvények
## mean(), std(), median(), variance() matek műveletek mátrixszal
