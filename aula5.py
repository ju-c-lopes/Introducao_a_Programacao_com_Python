lista = [12, 10, 5, 7, 11]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara', 'ariranha']

lista_animais[0] = 'macaco'  # trocamos a posição 0 'cachorro' por 'macaco'
print(lista_animais)

tupla_animais = tuple(lista_animais)
print(type(tupla_animais))
print(tupla_animais)
animais = list(tupla_animais)
print(animais)

# tupla = (1, 10, 12, 14)  # tupla são imutáveis, não conseguimos alterar o valor, e são definidas por parenteses()
# print(type(tupla))
# print(len(tupla))
# print(len(lista_animais))
# print(tupla[2])

#print(lista_animais[0])

#print(max(lista))

# lista_animais.sort()
# lista_animais.reverse()
# print(lista_animais)

"""
lista.sort()  # ordena a lista
lista_animais.sort()  # ordena a lista, sendo string, ordena em ordem afabetica
print(lista)
print(lista_animais)
"""
"""
if 'lobo' in lista_animais:
    print('Temos um lobo')
else:
    print('Ainda não tem um lobo')
    lista_animais.append('lobo')  # append é uma função da lista, e inclui um valor na lista
    print(lista_animais)
"""
#lista_animais.pop(0)  # retira o ultimo valor da lista se vazio, senão coloca a posição a ser retirada
#print(lista_animais)

#lista_animais.remove('elefante')  # remove um elemento da lista através do nome indicado
#print(lista_animais)
