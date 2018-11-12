# -*- coding: utf-8 -*

from timeit import default_timer as timer
import copy
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



class Tree(object):
	def __init__(self, r, iz, der):
		self.left = iz
		self.right = der
		self.label = r

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)
    return pila[-1]

def quitarDobleNegacion(f):
	# Elimina las dobles negaciones en una formula como arbol
	# Input: tree, que es una formula de logica proposicional
	# Output: tree sin dobles negaciones

	if f.right == None:
		return f
	elif f.label == '-':
		if f.right.label == '-':
			return quitarDobleNegacion(f.right.right)
		else:
			return Tree('-', \
						None, \
						quitarDobleNegacion(f.right)\
						)
	else:
		return Tree(f.label, \
					quitarDobleNegacion(f.left), \
					quitarDobleNegacion(f.right)\
					)

def reemplazarImplicacion(f):
    # Regresa la formula reemplazando p>q por -pOq
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

    if f.right == None:
        return f
    elif f.label == '-':
        return Tree('-', None, reemplazarImplicacion(f.right))
    elif f.label == '>':
        noP = Tree('-', None, reemplazarImplicacion(f.left))
        Q = reemplazarImplicacion(f.right)
        return Tree('O', noP, Q)
    else:
        return Tree(f.label, reemplazarImplicacion(f.left), reemplazarImplicacion(f.right))

def deMorgan(f):
    # Regresa la formula aplicando deMorgan -(pYq) por -pO-q
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

	if f.right == None:
		return f
	elif f.label == '-':
		if f.right.label == 'Y':
			print(u"La fórmula coincide negación Y")
			return Tree('O', \
						Tree('-', None, deMorgan(f.right.left)),\
						Tree('-', None, deMorgan(f.right.right))\
						)
		elif f.right.label == 'O':
			print(u"La fórmula coincide negación O")
			return Tree('Y', \
						Tree('-', None, deMorgan(f.right.left)),\
						Tree('-', None, deMorgan(f.right.right))\
						)
		else:
			return Tree('-', \
						None, \
						deMorgan(f.right) \
						)
	else:
		return Tree(f.label, \
					deMorgan(f.left),\
					deMorgan(f.right)\
					)

def distributiva(f):
    # Distribuye O sobre Ys: convierte rO(pYq) en (rOp)Y(rOq)
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

	if f.right == None:
		# print("Llegamos a una rama")
		return f
	elif f.label == 'O':
		# print("Encontramos O...")
		if f.left.label == 'Y':
			# print("... encontramos Y a la izquierda")
			P = f.left.left
			Q = f.left.right
			R = f.right
			return Tree('Y', \
						Tree('O', P, R), \
						Tree('O', Q, R)
						)
		if f.right.label == 'Y':
			# print("... encontramos Y a la derecha")
			R = f.left
			P = f.right.left
			Q = f.right.right
			return Tree('Y', \
						Tree('O', R, P), \
						Tree('O', R, Q)
						)
		else:
			# print("... pero no hay Y")
			# print("Pasamos a hijos de O")
			return Tree(f.label, \
						distributiva(f.left), \
						distributiva(f.right)
						)
	elif f.label == '-':
		# print("Pasamos a hijo de negacion")
		return Tree('-', \
					None, \
					distributiva(f.right)
					)
	else:
		# print("Pasamos a hijos de ", f.label)
		return Tree(f.label, \
					distributiva(f.left), \
					distributiva(f.right)
					)

def aplicaDistributiva(f):
    # Devuelve True si la distributiva de f es distinta a f
    # Input: tree, que es una formula de logica proposicional
    # Output: - True/False,
	# 		  - tree
	aux1 = Inorder(f)
	print("Se analiza: ", aux1)
	B = distributiva(f)
	aux2 = Inorder(B)
	print("Se obtuvo : ", aux2)
	if  aux1 != aux2:
		print(u"Hubo distribución")
		return True, B
	else:
		print(u"No hubo distribución")
		return False, f

def eliminaConjunciones(f):
    # Devuelve una lista de disyunciones de literales
    # Input: tree, que es una formula en CNF
    # Output: lista de cadenas
	if f.right == None:
		a = [Inorder(f)]
		print("Clausula unitaria positiva, ", a)
		return a
	elif f.label == 'O':
		return [Inorder(f)]
	elif f.label == 'Y':
		print(u"Dividiendo los lados de la conjunción")
		a = eliminaConjunciones(f.left)
		print("a, ", a)
		b = eliminaConjunciones(f.right)
		print("b, ", b)
		c = a + b
		print("c, ", c)
		return a + b
	else:
		if f.label == '-':
			if f.right.right == None:
				print("Clausula unitaria negativa")
				return [Inorder(f)]
			else:
				print("Oh, Oh, la formula no estaba en CNF!")

def complemento(l):
    # Devuelve el complemento de un literal
    # Input: l, que es una cadena con un literal (ej: p, -p)
    # Output: l complemento
	if '-' in l:
		return l[1:]
	else:
		return '-' + l

def formaClausal(f):
    # Obtiene la forma clausal de una formula en CNF
    # Input: tree, que es una formula de logica proposicional en CNF
    # Output: lista de clausulas

	# Primero elimino las conjunciones, obteniendo
	# una lista de disyunciones de literales
	print("Encontrando lista de disyunciones de literales...")
	aux = eliminaConjunciones(f)
	badChars = ['(', ')']
	conjuntoClausulas = []
	for C in aux:
		C = ''.join([x for x in C if x not in badChars])
		C = C.split('O')
		conjuntoClausulas.append(C)

	aux = []
	print(u"Eliminando cláusulas triviales...")
	for C in conjuntoClausulas:
		trivial = False
		for x in C:
			xComplemento = complemento(x)
			if xComplemento in C:
				print(u"Cláusula trivial encontrada")
				trivial = True
				break
		if not trivial:
			aux.append(C)

	print("Eliminando repeticiones...")
	# Eliminamos repeticiones dentro de cada clausula
	aux = [list(set(i)) for i in aux]
	# Eliminamos clausulas repetidas
	aux_set = set(tuple(x) for x in aux)
	aux = [list(x) for x in aux_set]

	conjuntoClausulas = aux

	return conjuntoClausulas

#################################################



def complemento(lit, letrasProp):
	if lit in letrasProp:
		comp = '-' + lit 
	else: 
		comp = lit.replace('-', '') 
	return comp

def unitPropagate(conjuntoClausulas, interp, letrasProp):
	for clause in conjuntoClausulas:
		if len(clause) == 1:
			if clause[0] in letrasProp:
				interp[clause[0]] = 'V'
			else: 
				interp[clause[0].replace('-', '')] = 'F'
			deleteClause(conjuntoClausulas, clause[0], letrasProp)
			unitPropagate(conjuntoClausulas, interp, letrasProp)
	return conjuntoClausulas, interp

def deleteClause(conjuntoClausulas, lit, letrasProp):
	
	cp = complemento(lit, letrasProp)

	for clause in conjuntoClausulas:
		if lit in clause:
	 		conjuntoClausulas.remove(clause)

	for clause in conjuntoClausulas:
		if cp in clause:
			clause.remove(cp)

	if len(conjuntoClausulas) > 0:
		if lit in conjuntoClausulas[len(conjuntoClausulas)-1]:
			conjuntoClausulas.remove(conjuntoClausulas[len(conjuntoClausulas)-1])


	return conjuntoClausulas

def DPLL(conjuntoClausulas, interp, letrasProp):

	empty = [] #cláusula vacía o conjunto vacío de cláusulas

	unitPropagate(conjuntoClausulas, interp, letrasProp) # propagación de la unidad

	print("Propagación terminada. Trabajando con el conjunto:")
	print(conjuntoClausulas)
	print("Y la interptetación:")
	print(interp)

	if empty in conjuntoClausulas: # si la cláusula vacía pertenece al conjunto de cláusulas
		return "la formula es insatisfacible con la interpretacion", interp # insatisfacible
	elif conjuntoClausulas == empty: # si el conjunto de cláusulas es vacío
		return "la formula es satisfacible con la interpretacion", interp # satisfacible
	else: # si el conjunto de cláusulas ni es vacío ni tiene la cláusula vacía		

		conjuntoAux = copy.deepcopy(conjuntoClausulas)  # crea una copia profunda del conjunto de cláusulas
		firstClause = conjuntoAux[0] # marca la primera cláusula en la copia
		intaux = copy.deepcopy(interp) # crea copia de la interpretación que recibió el algoritmo
		if firstClause[0] in letrasProp: # si el primer literal de la primera cláusula es una letra proposicional
			intaux[firstClause[0]] = 'V' # extiende la nueva interpretación añadiendo esa letra con V
			deleteClause(conjuntoAux, firstClause[0], letrasProp) # borra todas las cláusulas que tienen el literal y los complementos de las restantes
		elif firstClause[0] not in letrasProp: # si es la negación de una letra
			intaux[complemento(firstClause[0], letrasProp)] = 'F' # extiende la nueva interpretación añadiendo la letra con F
			deleteClause(conjuntoAux, firstClause[0], letrasProp) # borra todas las cláusulas que tienen el literal y los complementos de las restantes
			print(conjuntoAux)
		
		print("Marca de literal terminada: Trabajando con el conjunto:")
		print(conjuntoAux)
		print("Y la interptetación:")
		print(intaux)

		return DPLL(conjuntoAux, intaux, letrasProp)

		if DPLL(conjuntoAux, intaux, letrasProp) == ("insatisfacible", intaux):

			conjuntoAux2 = copy.deepcopy(conjuntoClausulas)  # crea una copia profunda del conjunto de cláusulas
			firstClause2 = conjuntoAux2[0] # marca la primera cláusula en la copia
			intaux2 = copy.deepcopy(interp) # crea copia de la interpretación 
			
			if firstClause[0] in letrasProp:
				intaux2[firstClause[0]] = 'F' # extiende la nueva interpretación añadiendo el primer literal de la primera cláusula con F
			else:
				intaux[complemento(firstClause[0], letrasProp)] = 'V' # extiende la nueva interpretación añadiendo el primer literal de la primera cláusula con V


			print("Marca de complemento terminada: Trabajando con el conjunto:")
			print(conjuntoAux2)
			print("Y la interptetación:")
			print(intaux2)

			deleteClause(conjuntoAux2, complemento(firstClause[0], letrasProp), letrasProp)	

			print('La fórmula es:')	

			return DPLL(conjuntoAux2, intaux2, letrasProp)

# Regla 2: no debe haber contacto entre barcos. Si una posición de un barco
# ocupa la casilla diagonal a la posición de otro barco, NO cuenta como
# contacto


    

# cadena = 'q--p->--'
# cadena = 'qpY-'
# cadena = 'rq-pO->'
# cadena = 'qpYprYO'
# cadena = 'qpYpr>O'
# cadena = 'pr>qpYO'
# cadena = 'q--qpYprYO->--'
# cadena = 'q-pYqp-YO'
# cadena = 'r-q-YpY'
# cadena = cadena + 'r-qYp-Y' + 'O'
# cadena = cadena + 'rq-Yp-Y' + 'O'
letrasProposicionales = []
for i in range (1,10):
    letrasProposicionales.append(str(i))

dec = ['A','B','C','D', 'E', 'F', 'G']

for i in dec:
    letrasProposicionales.append(i)

A = StringtoTree(conjunciones, letrasProposicionales)
print (u"Trabajando con la fórmula:\n ", Inorder(A))



A = quitarDobleNegacion(A)

print(u"La fórmula sin dobles negaciones es:\n ", Inorder(A))

A = reemplazarImplicacion(A)

print(u"La fórmula reemplazando implicaciones es:\n ", Inorder(A))

A = quitarDobleNegacion(A)

print(u"La fórmula sin dobles negaciones es:\n ", Inorder(A))

OK = True
while OK:
	aux1 = Inorder(A)
	print("Se analiza: ", aux1)
	B = deMorgan(A)
	B = quitarDobleNegacion(B)
	aux2 = Inorder(B)
	print("Se obtuvo : ", aux2)
	if  aux1 != aux2:
		print(u"Se aplicó deMorgan")
		OK = True
		A = B
	else:
		print(u"No se aplicó deMorgan")
		OK = False

OK = True
while OK:
	OK, A = aplicaDistributiva(A)

conjuntoClausulas = formaClausal(A)

print("Conjunto de disyunciones de literales:\n ", conjuntoClausulas)
sat=''

int1 = {}
sat,interpretacionesVerdaderas=DPLL(conjuntoClausulas,int1,letrasProposicionales)
print "DPLL Terminado"
end timer()
print u"El procedimiento demoró: ", end - start

if sat == 'la formula es satisfacible con la interpretacion':
    if len(interp) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(interp)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion as V
        contador = 1
        for i in interp:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"


		    
'''		    


letrasProp = ['p', 'q', 'r', 's', 'v', 'u']
int1 = {}
int2 = {}
int3 = {}
ejemplo = [['p', '-q', 'r'], ['-p', '-q', '-r'], ['-p', '-q', 'r'], ['p', '-q', '-r']]
ejemplo2 = [['-q', '-r'], ['-q', 'r']]
ejemplo3 = [['p', 'q'], ['p', '-q'], ['-p', 'q'], ['-p', '-r']]
prim = ejemplo2[0]
lit = prim[0]
sat = [['p', 'q'], ['r', 's']]
insat = [['p', 'q'], ['-p', 'q'], ['-q']]
print(DPLL(sat, int1, letrasProp))
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print(DPLL(insat, int2, letrasProp))
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print(DPLL(ejemplo3, int3, letrasProp),"Ejemplo 3")
'''

