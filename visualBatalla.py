#-*-coding: utf-8-*-

# David Moreno y Alejandro Velasco

# El problema a resolver es cómo disponer dos barcos en un tablero 4x4 de tal 
# forma que no sean contiguos. Se usarán literales para visualizar el problema:
# el literal es positivo sii hay una porción de un barco ocupando la casilla.
# Las porciones de barco están representadas con círculos. El tamaño de un 
# barco es 3 (si hay tres literales positivos contiguos, hay un barco allí).

# En esta visualización, se obtienen dos tableros: el primero es un ejemplo
# de un tablero satisfactorio; el segundo es un ejemplo de un tablero fallido.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 16;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere tambien un numero natural, para servir de indice del tablero,
# toda vez que puede solicitarse visualizar varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un numero natural


def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./4
    tangulos = []
    # Creo los cuadrados en el tablero

    tangulos.append(patches.Rectangle(*[(0, 0), step, step, step]))
    tangulos.append(patches.Rectangle(*[(0, step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(0, 3 * step), step, step, step]))

    tangulos.append(patches.Rectangle(*[(step, 0), step, step, step]))
    tangulos.append(patches.Rectangle(*[(step, step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(step, 3 * step), step, step, step]))

    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step, step]))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(2 * step, 3 * step), step, step, step]))

    tangulos.append(patches.Rectangle(*[(3 * step, 0), step, step, step]))
    tangulos.append(patches.Rectangle(*[(3 * step, step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(3 * step, 2 * step), step, step, step]))
    tangulos.append(patches.Rectangle(*[(3 * step, 3 * step), step, step, step]))


    # Creo las líneas del tablero
    for j in range(4):
        locacion = j * step
        # Crea lineas horizontales en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea lineas verticales en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de círculo
    arr_img = plt.imread("circulo.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.02)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.12, 0.87]
    direcciones[2] = [0.37, 0.87]
    direcciones[3] = [0.62, 0.87]
    direcciones[4] = [0.87, 0.87]

    direcciones[5] = [0.12, 0.62]
    direcciones[6] = [0.37, 0.62]
    direcciones[7] = [0.62, 0.62]
    direcciones[8] = [0.87, 0.62]

    direcciones[9] = [0.12, 0.37]
    direcciones[10] = [0.37, 0.37]
    direcciones[11] = [0.62, 0.37]
    direcciones[12] = [0.87, 0.37]

    direcciones[13] = [0.12, 0.12]
    direcciones[14] = [0.37, 0.12]
    direcciones[15] = [0.62, 0.12]
    direcciones[16] = [0.87, 0.12]

    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()
    fig.savefig("tablero_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

script, data_archivo = argv

with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando tablero:", l
        dibujar_tablero(l, contador)
        contador += 1

csv_file.close()
