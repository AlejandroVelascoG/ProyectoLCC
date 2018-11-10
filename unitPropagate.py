# -*- coding: utf-8 -*
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
	for clause in conjuntoClausulas:
		if complemento(lit, letrasProp) in clause:
			clause.remove(complemento(lit, letrasProp))
	for clause in conjuntoClausulas:
		if lit in clause:
			conjuntoClausulas.remove(clause)
"""def literalpuro(conjuntoClausulas):
    for i in range(len(letrasProp)):
        
        if letrasPro[i] in conjunto and complemento(letrasPro[i], letrasProp) in conjunto:
            for j in range(len(conjuntoClausulas)):
                if letrasPro[i] in conjunto:
                    remove.conjuntoClausulas(j) and remove.conjuntoClausulas(p for p in complemento(letraPro[i], letrasProp))
                    

    return conjuntoClausulas
    """
            
            
			


			

def DPLL(conjuntoClausulas, interp, letrasProp):
	emptyClause = []
	unitPropagate(conjuntoClausulas, interp, letrasProp)
	if emptyClause in conjuntoClausulas:
		return "insatisfacible", interp
	elif conjuntoClausulas == emptyClause:

		return "satisfacible", interp
	else:
		clause = conjuntoClausulas[0]
		interp[clause[0]] = 'V'
		deleteClause(conjuntoClausulas, clause[0], letrasProp)
#	
#		deleteClause(conjuntoClausulas, clause[0], letrasProp)


letrasProp = ['p', 'q', 'r', 's', 'v', 'u']
int1 = {}
int2 = {}
conjunto = [['-p', '-q'], ['p', 'r'], ['q'], ['s', 'u', 'v'], ['-u']]
conj2 = [['p']]
print(conjunto)
print(conj2)
unitPropagate(conjunto, int1, letrasProp)
unitPropagate(conj2, int2, letrasProp)
print('-----------------------------------')
print(conjunto)
print(int1)
print('-----------------------------------')
print(conj2)
print(int2)
print('-----------------------------------')


#print(DPLL(conj2, int2, letrasProp))
