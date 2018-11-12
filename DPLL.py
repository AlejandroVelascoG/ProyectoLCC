# -*- coding: utf-8 -*
import copy

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
			conjuntoAux.remove(conjuntoAux[0])
			deleteClause(conjuntoAux, firstClause[0], letrasProp) # borra todas las cláusulas que tienen el literal y los complementos de las restantes
		elif firstClause[0] not in letrasProp: # si es la negación de una letra
			intaux[complemento(firstClause[0], letrasProp)] = 'F' # extiende la nueva interpretación añadiendo la letra con F
			conjuntoAux.remove(conjuntoAux[0])
			deleteClause(conjuntoAux, firstClause[0], letrasProp) # borra todas las cláusulas que tienen el literal y los complementos de las restantes
			print(conjuntoAux)
		
		print("Marca de literal terminada: Trabajando con el conjunto:")
		print(conjuntoAux)
		print("Y la interptetación:")
		print(intaux)

		return DPLL(conjuntoAux, intaux, letrasProp)

		if DPLL(conjuntoAux, intaux, letrasProp) == ("la formula es insatisfacible con la interpretacion", intaux):

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

			conjuntoAux2.remove(conjuntoAux2[0])
			deleteClause(conjuntoAux2, complemento(firstClause[0], letrasProp), letrasProp)	

			return DPLL(conjuntoAux2, intaux2, letrasProp)	


# letrasProp = ['p', 'q', 'r', 's', 'v', 'u']
# int1 = {}
# int2 = {}
# int3 = {}
# ejemplo = [['p', '-q', 'r'], ['-p', '-q', '-r'], ['-p', '-q', 'r'], ['p', '-q', '-r']]
# ejemplo2 = [['-q', '-r'], ['-q', 'r']]
# ejemplo3 = [['p', 'q'], ['p', '-q'], ['-p', 'q'], ['-p', '-r']]
# prim = ejemplo2[0]
# lit = prim[0]
# sat = [['p', 'q'], ['r', 's']]
# insat = [['p', 'q'], ['-p', 'q'], ['-q']]
# print(DPLL(sat, int1, letrasProp))
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print(DPLL(insat, int2, letrasProp))
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
# print(DPLL(ejemplo3, int3, letrasProp))


	

