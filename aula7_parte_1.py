"""
Método e função

Função -> tudo que retorna um valor
Método -> tudo o que não retorna
"""

# Método é declarado por "def"

print('"""\nMétodo e função\n\nFunção -> tudo que retorna um valor\nMétodo -> tudo o que não retorna\n"""\n\n# Método é declarado por "def"\n')

def soma(a, b):
        return a + b


def subtracao(a, b):
        return a - b


def multiplicacao(a, b):
        return a * b


def divisao (a, b):
        return a / b


print('def soma(a, b):\n    return a + b\n')
print('def subtracao(a, b):\n    return a - b\n')
print('def multiplicacao(a, b)\n    return a * b\n')
print('def divisao (a, b):\n    return a / b\n')

print("\nprint('Soma: {}'.format(soma(1, 2)))")
print('Soma: {}'.format(soma(1, 2)))
print("\nprint('Soma: {}'.format(soma(3, 4)))")
print('Soma: {}'.format(soma(3, 4)))
print("\nprint('Subtração: {}'.format()(subtracao(10, 2)))")
print('Subtração: {}'.format(subtracao(10, 2)))
print("\nprint('Multiplicação: {}'.format(multiplicacao(10, 2)))")
print('Multiplicação: {}'.format(multiplicacao(10, 2)))
print("\nprint('Divisao: {}'.format(divisao(10, 2)))")
print('Divisao: {}'.format(divisao(10, 2)))
