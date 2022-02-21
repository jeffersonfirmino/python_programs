
salario_minimo= 880.00
percentual_aumento= (910.40-salario_minimo)*100/salario_minimo
novo_salario_bruto= salario_minimo+percentual_aumento
novo_salario_liquido= (novo_salario_bruto)-(novo_salario_bruto/100*8)
print '\n## Salário mínimo 2016!'
print '\n%.2f'%(salario_minimo)

print '\n## Previsão de dados novo salário##'
print '\n Salário Bruto : %2f'%(novo_salario_bruto)
print '\n Salário Líquido: %.2f'%(novo_salario_liquido)


