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

conjunciones = '4-5-6-7-YYY123YY>' + conjunciones + 'Y'
conjunciones = '1-5-7-8-7-YYY234YY>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-8-9-10-11-YYY567YY>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-5-10-11-12-YYY678YY>' + conjunciones + 'Y'
conjunciones = '5-6-7-12-13-14-15-16YYY91011YY>' + conjunciones + 'Y'
conjunciones = '6-7-8-9-13-14-15-YYY101112YY>' + conjunciones + 'Y'
conjunciones = '10-11-12-16-YYY131415YY>' + conjunciones + 'Y'
conjunciones = '9-10-11-13-YYY141516YY>' + conjunciones + 'Y'
conjunciones = '2-6-10-13-YYY159YY>' + conjunciones + 'Y'
conjunciones = '1-5-9-14-3-7-11-YYY2610YY>' + conjunciones + 'Y'
conjunciones = '2-6-10-15-14-8-12-YYY3711YY>' + conjunciones + 'Y'
conjunciones = '3-7-11-16-YYY4812YY>' + conjunciones + 'Y'
conjunciones = '1-6-10-14-YYY5913YY>' + conjunciones + 'Y'
conjunciones = '5-9-13-2-7-11-15-YYY61014YY>' + conjunciones + 'Y'
conjunciones = '6-10-14-3-8-12-16-YYY71115YY>' + conjunciones + 'Y'
conjunciones = '4-7-11-15-YYY81216YY>' + conjunciones + 'Y'

A = T.StringtoTree(conjunciones, letrasProposicionales)
print (T.Inorder(A))