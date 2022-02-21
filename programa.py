#coding: utf-8

s = raw_input().split()
palindromo = ''

for i in range(len(s)-1,-1,-1):
	palindromo += s[i]
	
if palindromo==s:
	print '%s é palíndromo' % (palindromo)

else:
	print '%s não é palíndromo' % (s)
