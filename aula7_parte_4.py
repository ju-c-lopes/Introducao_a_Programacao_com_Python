class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if televisao.ligada:
            self.canal += 1

    def diminui_canal(self):
        if televisao.ligada:
            self.canal -= 1

televisao = Televisao()
print('Televisão ligada? {}\n Apertando power'.format(televisao.ligada))
televisao.power()
print('Televisão ligada? {}\n Apertando power'.format(televisao.ligada))
televisao.power()
print('Televisão ligada? {}'.format(televisao.ligada))
televisao.power()
print('\nTelevisão ligada? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
print('televisao.aumenta_canal()\ntelevisao.aumenta_canal()')
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
print('televisao.diminui_canal()')
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))
