
a = int(input('Primeiro bim: '))
while a > 10:
    a = int(input('Você digitou nota errada. Primeiro bim: '))
b = int(input('Segundo bim: '))
while b > 10:
    b = int(input('Você digitou nota errada. Segundo bim: '))
c = int(input('Terceiro bim: '))
while c > 10:
    c = int(input('Você digitou nota errada. Terceiro bim: '))
d = int(input('Quarto bim: '))
while d > 10:
    d = int(input('Você digitou nota errada. Quarto bim: '))
media = (a+b+c+d) / 4
print('Média: {}'.format(media))

"""
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('Foi digitado uma nota inválida')
"""
"""
a = int(input('Entre com um valor: '))
b = int(input('Entre com outro valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print('foi digitado um número par')
else:
    print('Nenhum numero par foi digitado')

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
print('final do programa')
"""

