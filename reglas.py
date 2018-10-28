# coding=utf-8

# Este código ubica los dos barcos en el tablero

import random

# Posiciones inciales barcos horizontales:

Hor = [1, 2, 5, 6, 9, 10, 13, 14]

# Posiciones inciales barcos verticales:

Ver = [1, 2, 3, 4, 5, 6, 7, 8]

barcos = [] # lista que guardará las posiciones de los barcos

i = 0

for i in range (0,2):

	a = random.uniform(0,1) # número que determina si un barco es horizontal o vertical
	b = random.randint(0,7) # número con el que se elige una posición inicial

	if a<=0.5:	# Si a<=0.5, el barco será horizontal

		barcos.append(Hor[b])
		barcos.append(Hor[b]+1)
		barcos.append(Hor[b]+2)

	else: # si a>0.5, el barco será vertical:
		
		barcos.append(Ver[b])
		barcos.append(Ver[b]+4)
		barcos.append(Ver[b]+8)

	++i

	barcos=map(str,barcos) # pasa las posiciones de los barcos a string

tablero = [] # lista que guardará el tablero

for i in range(1,17):
		if str(i) not in barcos: 		 # si una posición del tablero no está en la lista de las posiciones de los barcos
			tablero.append('-' + str(i)) # marca esa posición con la negación para indicar que ahí no hay nada 
		else:
			tablero.append(str(i)) 		 # guarda la posición del barco en el tablero
print (barcos)
print (tablero)

