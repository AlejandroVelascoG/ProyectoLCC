#-*-coding: utf-8-*-

# David Moreno y Alejandro Velasco
# código para resolver el problema de los barcos 

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente dos barcos de tamaño 3

# Creo las letras proposicionales

letrasProposicionales = []
for i in range (1,10):
    letrasProposicionales.append(str(i))

dec = ['A','B','C','D', 'E', 'F', 'G']

for i in dec:
    letrasProposicionales.append(i)


# Posiciones inciales barcos horizontales:

Hor = [1, 2, 5, 6, 9, 'A', 'D', 'E']

# Posiciones inciales barcos verticales:

Ver = [1, 2, 3, 4, 5, 6, 7, 8]

barcos = [] # lista de todos los barcos posibles
    
for j in Hor: # mete a barcos todos los barcos horizontales posibles
    
    bar_hor = []

    if j <= 6:
        bar_hor.append(str(j))
        bar_hor.append(str((j)+1))
        bar_hor.append(str((j)+2))
    if j == 9:
        bar_hor.append('9')
        bar_hor.append('A')
        bar_hor.append('B')
    if j == 'A':
        bar_hor.append('A')
        bar_hor.append('B')
        bar_hor.append('C')
    if j == 'D':
        bar_hor.append('D')
        bar_hor.append('E')
        bar_hor.append('F')
    if j == 'E':
        bar_hor.append('E')
        bar_hor.append('F')
        bar_hor.append('G')

    barcos.append(bar_hor)



for k in Ver: # mete a barcos todos los barcos horizontales verticales
    
    bar_ver = []
    
    if k == 1:
        bar_ver.append(str(k))
        bar_ver.append('5')
        bar_ver.append('9')
    if k == 2:
        bar_ver.append('2')
        bar_ver.append('6')
        bar_ver.append('A')
    if k == 3:
        bar_ver.append('3')
        bar_ver.append('7')
        bar_ver.append('B')
    if k == 4:
        bar_ver.append('4')
        bar_ver.append('8')
        bar_ver.append('C')
    if k == 5:
        bar_ver.append('5')
        bar_ver.append('9')
        bar_ver.append('D')
    if k == 6:
        bar_ver.append('6')
        bar_ver.append('A')
        bar_ver.append('E')
    if k == 7:
        bar_ver.append('7')
        bar_ver.append('B')
        bar_ver.append('F')
    if k == 8:
        bar_ver.append('8')
        bar_ver.append('C')
        bar_ver.append('G')

    barcos.append(bar_ver)


tablero = []
for i in range (1,17):
    tablero.append(str(i))

conjunciones = '' # Para ir guardando las disyunciones de trios de literales
inicial = True # Para inicializar la primera conjuncion

for p in barcos:
    aux1 = [x for x in  barcos if x != p] # Todos los barcos excepto p
    # print "aux1: ", aux1
    for q in aux1:
            literal = q[0] + q[1] + q[2] + p[0] + p[1] + p[2] + 'Y' + 'Y' + 'Y' + 'Y' + 'Y'
            lista_barco = [q[0], q[1], q[2], p[0], p[1], p[2]]
            aux2 = [x + '-' for x in letrasProposicionales if x not in lista_barco]
            print(aux2)
            for k in aux2:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

# Regla 2: no debe haber contacto entre barcos. Si una posición de un barco
# ocupa la casilla diagonal a la posición de otro barco, NO cuenta como
# contacto

conjunciones = '4-5-6-7-YYY123YY>' + conjunciones + 'Y'
conjunciones = '1-5-6-7-8-YYY234YY>' + conjunciones + 'Y'
conjunciones = '1-2-3-8-9-A-B-YYY567YY>' + conjunciones + 'Y'
conjunciones = '2-3-4-5-A-B-C-YYY678YY>' + conjunciones + 'Y'
conjunciones = '5-6-7-C-D-E-F-YYY9ABYY>' + conjunciones + 'Y'
conjunciones = '6-7-8-9-E-F-G-YYYABCYY>' + conjunciones + 'Y'
conjunciones = '9-A-B-C-G-YYYDEFYY>' + conjunciones + 'Y'
conjunciones = '9-A-B-C-D-YYYEFGYY>' + conjunciones + 'Y'
conjunciones = '2-6-A-D-E-YYY159YY>' + conjunciones + 'Y'
conjunciones = '1-5-9-E-3-7-B-YYY26AYY>' + conjunciones + 'Y'
conjunciones = '2-6-A-F-4-8-C-YYY37BYY>' + conjunciones + 'Y'
conjunciones = '3-7-B-G-YYY48CYY>' + conjunciones + 'Y'
conjunciones = '1-6-A-E-YYY59DYY>' + conjunciones + 'Y'
conjunciones = '5-9-D-2-7-B-F-YYY6AEYY>' + conjunciones + 'Y'
conjunciones = '6-A-E-3-8-C-G-YYY7BFYY>' + conjunciones + 'Y'
conjunciones = '4-7-B-F-YYY8CGYY>' + conjunciones + 'Y'


A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"
