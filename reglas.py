# coding=utf-8

import Tableaux as T

letrasProposicionales = []
for i in range (1,17):
	letrasProposicionales.append(str(i))


# Posiciones inciales barcos horizontales:

Hor = [1, 2, 5, 6, 9, 10, 13, 14]

# Posiciones inciales barcos verticales:

Ver = [1, 2, 3, 4, 5, 6, 7, 8]

barcos = [] # lista de todos los barcos posibles
	
for j in Hor: # mete a barcos todos los barcos horizontales posibles
	bar_hor = []
	bar_hor.append(j)
	bar_hor.append((j)+1)
	bar_hor.append((j)+2)
	barcos.append(bar_hor)

for k in Ver: # mete a barcos todos los barcos horizontales verticales
	bar_ver = []
	bar_ver.append(k)
	bar_ver.append((k)+4)
	bar_ver.append((k)+8)
	barcos.append(bar_ver)

tablero = []
for i in range (1,17):
	tablero.append(str(i))

conjunciones = '' # Para ir guardando las disyunciones de trios de literales
inicial = True # Para inicializar la primera conjuncion

for p in barcos:
    aux1 = [x for x in  barcos if x != p] # Todos los barcos excpeto p
    # print "aux1: ", aux1
    for q in aux1:
            literal = str(q[0]) + str(q[1]) + str(q[2]) + str(p[0]) + str(p[1]) + str(p[2]) + 'Y' + 'Y' + 'Y' + 'Y' + 'Y'
            lista_barco = [str(q[0]), str(q[1]), str(q[2]), str(p[0]), str(p[1]), str(p[2])]
            aux2 = [x + '-' for x in tablero if x not in lista_barco]
            for k in aux2:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

A = T.StringtoTree(conjunciones, letrasProposicionales)
print (T.Inorder(A))