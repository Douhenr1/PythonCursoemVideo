#Operadores Aritméticos
# + - * /
# ** potencia
# // divisão inteira
# % resto da divisão

# 5+2==
# 5-2==
# 5*2==
# 5/2==
# 5**2==
# 5//2==
# 5%2==

#Ordem de precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -


n1 = int (input('Primeiro valor:'))
n2 = int (input('Segundo valor:'))

s = n1 + n2
ss = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
resto = n1 % n2

print('A soma é {}, /n o produto é {} e a divisão {}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potencia {}' .format(di, e))
print('O resto da divisão acima é {}'. format(resto))