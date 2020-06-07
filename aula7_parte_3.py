
class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(f'Soma: {calculadora.soma(10, 2)}')
print(f'Subtração: {calculadora.subtracao(5, 3)}')
print(f'Multiplicação: {calculadora.multiplicacao(10, 5)}')
print(f'Divisão: {calculadora.divisao(100, 2)}')