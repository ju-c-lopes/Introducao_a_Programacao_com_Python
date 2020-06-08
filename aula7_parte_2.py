
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(f'Valor A: {calculadora.valor_a}')
    print(f'Valor B: {calculadora.valor_b}')
    print(f'Soma: {calculadora.soma()}')
    print(f'Subtração: {calculadora.subtracao()}')
    print(f'Multiplicação: {calculadora.multiplicacao()}')
    print(f'Divisão: {calculadora.divisao()}')