#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
import random
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres caballos
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion



#maneras de tener un barco







LetProp = []
for i in range (1, 16):
    LetProp.append(i)


# Posiciones inciales barcos horizontales:

Hor = [1, 2, 5, 6, 9, 10, 13, 14]

# Posiciones inciales barcos verticales:

Ver = [1, 2, 3, 4, 5, 6, 7, 8]

barcos = [] # lista que guardará las posiciones de los barcos

i = 0

for i in range (0,2):

    a = random.uniform(0,1) # número que determina si un barco es horizontal o vertical
    b = random.randint(0,7) # número con el que se elige una posición inicial

    if a<=0.5:  # Si a<=0.5, el barco será horizontal

        barcos.append(Hor[b])
        barcos.append(Hor[b]+1)
        barcos.append(Hor[b]+2)

    else: # si a>0.5, el barco será vertical:
        
        barcos.append(Ver[b])
        barcos.append(Ver[b]+4)
        barcos.append(Ver[b]+8)

    ++i
    barcosting=map(str,barcos)



print (barcosting)



if barcos==(1,5,9):
    (13,2,6,10)=False

        
    
elif barcos==(5,9,13):

    (1,6,10,14)=False

elif barcos==(4,8,12):

    (3,7,11,16)=False
elif barcos==(8,12,16):

    (4,7,11,15)=False

elif barcos==(16,15,14):

    (13,10,11,12)=False
elif barcos==(15,14,13):

    (16,9,10,11)=False
elif barcos==(13,9,5):

    (1,6,10,14)=False
elif barcos==(9,5,1):

    (13,10,6,2)=False
elif barcos==(2,6,10):

    (1,5,9,14,3,7,11,15,13)=False
elif barcos==(6,10,14):

    (5,9,13,1,2)=False
elif barcos==(3,7,11):

    (2,6,10,4,8,12,14)=False
elif barcos==(7,11,15):

    (8,12,16,6,10,14,3,4)=False
elif barcos==(9,10,11):

    (13,14,15,16,12,5,6,7,8)=False
elif barcos==(10,11,12):

    (13,14,15,16,9,5,6,7,8)=False
elif barcos==(5,6,7):

    (1,2,3,4,8,9,10,11,12)=False
elif barcos==(6,7,8):

    (5,1,2,3,4,9,10,11,12)=False

elif barcos==(15,11,7):

    (16,12,8,4,3,14,10,6,2)=False
elif barcos==(11,7,3):

    (16,12,8,4,15,2,6,10,11)=False
elif barcos==(14,10,6):

    (2,13,9,5,1,15,11,7,3)=False

elif barcos==(10,6,2):

    (14,3,7,11,15,1,5,9,13)=False

elif barcos==(8,7,6):

    (4,3,2,1,5,12,11,10,9)=False

elif barcos==(7,6,5):

    (4,3,2,1,8,12,11,10,9)=False
elif barcos==(12,11,10):

    (9,16,15,14,13,8,7,6,5)=False

elif barcos==(11,10,9):
    12=False and 5=False and 6=False and 7=False and 8=False and 13=False and 14=False and 15=False and 16=False

    (12,5,6,7,8,13,14,15,16)=False 





        # print "Conjunciones: ", conjunciones

# Regla 2: Ningun caballo debe poder atacar a otro

       

# Creo la formula como objeto

A = T.StringtoTree(barcosting, letrasProposicionales)
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