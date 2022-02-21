#coding: utf -8

def soma_matriz_interna(matriz, inicio, fim):
	saida = 0
	
	# movimento em x
	comecox = inicio[0]
	fimx = fim[0]
	
	# movimento em y
	comecoy = inicio[1]
	fimy = fim[1]
	
	while True: 	
		
		if comecox == fimx and comecoy == fimy:
			saida += matriz[comecox][comecoy]
			break
		
		else:
			saida += matriz[comecox][comecoy] 	 	
			comecoy += 1
		
		if comecoy > fimy:
			comecox += 1
			comecoy = inicio[1]
		
	return saida 
	

M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
assert soma_matriz_interna(M2, (1,1),(2,2)) == 5 + 6 + 8 + 9
