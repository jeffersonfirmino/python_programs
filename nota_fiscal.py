print('Resumo da Nota Fiscal, favor introduzir os valores conforme o especificado:')

data = str(raw_input('\n Digite a data referente, neste formato dd/mm/aaaa: '))

valor_total = float(raw_input('\n Digite o valor total  de compras: R$ '))

quantidade_de_produtos = int(raw_input('\n Digite a quantidade de produtos: '))

media = valor_total / quantidade_de_produtos

print '\n Data da compra: %s' %(data)

print '\n O valor total da compra foi de: R$ %.2f. A média do preço dos produtos é de: R$ %.2f por unidade.' %(valor_total,media)



