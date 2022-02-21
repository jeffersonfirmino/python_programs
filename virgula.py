#coding: utf-8

frase = raw_input()
lista = []
i = int(raw_input())
j = int(raw_input())

for l in frase:
    lista.append(l)

for k in range (i,j):
    if lista[k] == ' ':
        lista[k] = ','
        
g = ''

for m in lista:
    g += m

print g
