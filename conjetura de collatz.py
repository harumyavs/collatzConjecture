#!/usr/bin/env python
# coding: utf-8
# In[75]:
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(2)
# generate some integers
numeros_validos = [] #150 numeros con los cuales se cumple la ley de Benford cuando se aplica la conjetura de Collatz
numeros_invalidos = [] # 150 numeros con los cuales no se cumple la ley de Benford al aplicar la conjetura de Collatz
a = 0
while a < 150 :
	value = randint(1, 100000)
	inicio = value
    #Collatz
	arr = [0]
	for _ in range(10):
		arr.append(0)
	while value != 1:
		digito = value;
		while digito > 10:
			digito /= 10
		arr[int(digito)] += 1
		if value % 2 == 0:
			value /= 2
		else:
			value = value * 3 + 1
	i = 2
	valido = 0
# Se utiliza esta pseudo ley de Benford porque no existe secuencia de Collatz que cumpla con la ley exacta
	#Ley de Benford no se cumple con exactitud
	if arr[1] + arr[2] + arr[3]   > arr[4] + arr[5] + arr[6] and arr[4] + arr[5] + arr[6] > arr[7] + arr[8] + arr[9]:
		valido = 1
	if valido == 1:
		if len(numeros_invalidos) < 200:
			numeros_invalidos.append(inicio)
	if valido == 0:
		numeros_validos.append(inicio)
	if valido == 1:
		a -= 1
	a += 1

print("\nLos numeros invalidos son: ")
print(" ")
for x in range(150):
	print(numeros_invalidos[x])
print("\nLos numeros validos son: ")

for x in range(150):
	print(numeros_validos[x])
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




