"""
Características:
lista -> listas são feitas usando colchetes "[]"
tuplas -> são feitas usando parenteses "()"
conjuntos -> são feitos usando chaves "{}" -> conjuntos são do tipo set(usando print type)
    conjuntos não repetem valores
"""

conjunto = {1, 2, 3, 4}
print(type(conjunto))
print(conjunto)

print('conjunto.add(5)')
conjunto.add(5)
print(conjunto)

print('conjunto.discard(2)')
conjunto.discard(2)
print(conjunto)

# Podemos também fazer união de conjuntos, veja abaixo

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
print('\nconjunto1 = {1, 2, 3, 4, 5}\nconjunto2 = {5, 6, 7, 8}\nconjunto_uniao = conjunto1.union(conjunto2)')
print(f'União: {conjunto_uniao}\n')

# Podemos também fazer a intersecção de conjuntos, veja abaixo
print('\nconjunto_interseccao = conjunto1.intersection(conjunto2)')
conjunto_interseccao = conjunto1.intersection(conjunto2)
print(f'Intercecção: {conjunto_interseccao}\n')

# Podemos fazer também a diferença entre conjuntos, no exemplo abaixo,
# o resultado será somente o que tem no conjunto 1

print('\nconjunto_diferenca1 = conjunto1.difference(conjunto2)')
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print(f'Diferença entre 1 e 2: {conjunto_diferenca1}')

# o resultado do exemplo abaixo será somente o conteudo que tem no conjunto dois

conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('\nconjunto_diferenca2 = conjunto2.difference(conjunto1)')
print(f'Diferença entre 2 e 1: {conjunto_diferenca2}\n')

# Diferença simétrica -> Tudo o que não tem nos dois

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('\nconjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2) # Reparem que imprimirá sem o "5"')
print(f'Diferença simétrica entre 1 e 2: {conjunto_diff_simetrica}\n')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('\nconjunto_subset = conjunto_a.issubset(conjunto_b) # Retornará um valor booleano')
print(f'A é subconjunto de B? {conjunto_subset}')

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('\nconjunto_subset = conjunto_b.issuperset(conjunto_a) # Retornará um valor booleano')
print(f'B é superconjunto de A? {conjunto_superset}\n')

print('\nExemplo de uso dos conjuntos:')
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
lista_animais = set(lista)
print(f"\nlista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']\nlista_animais = set(lista)")
print(lista_animais)
print('\nConvertendo novamente o conjunto pra lista, teremos a lista sem duplicidade de valores')
lista_animais = list(lista_animais)
print('lista_animais = list(lista_animais)')
print(lista_animais)