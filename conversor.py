print '\t Programa que converte de Fahrenheit para Kelvin e Celsius!'
f= float(raw_input('\n Digite o valor da temperatura em Fahrenheit: '))
c= (f-32)*5/9
k= c+273.15

print '\n O valor em Fahrenheit �: %.3f. F' %(f)
print '\n O valor em Celsius �: %.3f C' %(c)
print '\n O valor em Kelvin �: %.3f K' %(k)
