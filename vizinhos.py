#coding:utf-8

def soma_diminui_vizinhos(lista):
	if lista != []:
		soma = lista[0]
		for i in range(len(lista)-1):
			if i % 2 == 0 :
				soma += lista[i+1]
			
			if i % 2 != 0 :
				soma -= lista[i+1]
		return soma 
	else:
		soma = 0
		return soma  
	
	

