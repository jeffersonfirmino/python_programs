identificador = str(raw_input('\nDigite seu identificador de voo: '))
horario = raw_input('\nDigite o hor�rio neste formato (hh:mm): ')
assento = int(raw_input('\nDigite o n�mero do assento: '))
portao = int(raw_input('\nDigite o n�mero do port�o: '))
preco_sem_imposto = float(raw_input('\nDigite o valor sem imposto: '))
preco_total = float(raw_input('\nDigite o valor com o imposto: '))
porcentagem_de_imposto = (preco_total - preco_sem_imposto) * 100 / preco_sem_imposto

print '\n### Cart�o de Embarque ###'
print '\nIdentificador do voo: %s. Hor�rio: %s. Assento: %d. Port�o: %d.' %(identificador,horario,assento,portao)
print '\nTotal de Imposto: %.2f%%.' %(porcentagem_de_imposto)
