#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 4x4 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere tambien un numero natural, para servir de indice del tablero,
# toda vez que puede solicitarse visualizar varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un numero natural

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import os

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
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de caballo
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
        if '-' not in l:
            if l=='A':
                l=10
            elif l=='B':
                l=11
            elif l=='C':
                l=12
            elif l=='D':
                l=13
            elif l=='E':
                l=14
            elif l=='F':
                l=15
            elif l=='G':
                l=16
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()
    d = 'Soluciones/'
    try:
        os.makedirs(d)
        print "Creando " + d
    except OSError:
        if not os.path.isdir(d):
            raise
    fig.savefig(d + "tablero_" + str(n) + ".png")
    print "Imagenes creadas! Verificar la carpeta " + d
