
from aula7_parte_4 import Televisao
from aula7_parte_2 import Calculadora
from aula8_contador_letras import contador_letras, teste


if __name__ == '__main__':
    calculadora = Calculadora(3, 8)
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())
    