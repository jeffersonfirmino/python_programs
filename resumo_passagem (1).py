# coding: utf-8
identificador= int(raw_input())
horario= raw_input()
assento= raw_input()
portao= raw_input()
preco_sem_imposto= float(raw_input())
preco_total= float(raw_input())
porcentagem_de_imposto= ((preco_total - preco_sem_imposto)/ preco_sem_imposto)*100

print '### Cartão de Embarque ###'
print 'Identificador do voo: %d. Horário: %s. Assento: %s. Portão: %s.' %(identificador,horario,assento,portao)
print 'Total de Imposto: %f%%.' %(porcentagem_de_imposto)


