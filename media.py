print('Resumo da Nota Fiscal, favor introduzir os valores conforme o especificado:')
print('')

data = str(input('Digite a data referente, neste formato dd/mm/aaaa: '))

print('')

valor_total = float(input('Digite o valor total  de compras: R$ '))

print('')

quantidade_de_produtos = float(input('Digite a quantidade de produtos: '))

media = valor_total / quantidade_de_produtos

print('')

print ('A data de hoje e: %s' %(data))
print('')

print ('O valor total da compra foi de: R$ %.2f' %(valor_total))
print('')

print ('A média dos preços dos produtos é de: R$ %.2f por unidade.' %(media))

