#Autor Daniel Felipe Bueno Calderón
import random
def matrixAverage(n, m):
  if (n > 2 and m > 2):
   # the bidimentional array  with random number beetween 1 and  n+m has been created
   matrix = [[random.randint(1, n*m) for x in range (m)] for  j in range (n)]
   
   for i in matrix:
    print (i)

   arrayAverage = [0 for i in range (m)]

   summation = 0
   counter = 0
   for  k in range (m):
     for  j in range (n):
      arrayAverage [k] = arrayAverage[k] + matrix[j][k]
     if (not(k%2 == 0)):
       summation = summation + arrayAverage [k]
       counter = counter + 1

   print ("= = = = = =")
   print (arrayAverage)
   print ("= = = = = =")
   average = summation/counter
   print ("Promedio columnas pares =" + str(average))
   arrayGreaterThatAverage = []
   
   for l in arrayAverage:
     if (l > average):
      arrayGreaterThatAverage.append(l) 

   print("Cantidad de columnas cuyo total es mayor que "+ str(average) +" = " + str(len(arrayGreaterThatAverage)))
   # Return the column summation greater than the average of even columns
   return arrayGreaterThatAverage
  
  else:
    print ("El valor de los indices de la matriz deben ser mas grandes que 2")

test = matrixAverage(3,4)
