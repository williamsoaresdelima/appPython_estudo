class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal =5

    def power(self):
        if(self.ligada):
            self.ligada=False
        else:
            self.ligada=True

    def aumenta_canal(self):
        if(self.ligada):
            self.canal +=1

    def diminui_canal(self):
        if (self.ligada):
            self.canal -=1
    #
    # if __name__ == '__main__':
    #     tv = Televisao()
    #     print(tv.ligada)
    #     tv.power()
    #     print(tv.ligada)
    #     tv.power()
    #     print(tv.ligada)
    #
    #     tv.power()
    #     print(tv.ligada)
#
# print('Canal {}'.format(tv.canal))
# tv.aumenta_canal()
# tv.aumenta_canal()
# print('Canal {}'.format(tv.canal))
# tv.diminui_canal()
# print('Canal {}'.format(tv.canal))
#
# def minha_funcao(numero):
#     if numero % 2 == 0:
#         return '{} é par'.format(numero)
#     else:
#         return '{} é ímpar'.format(numero)
#     return "zero é neutro"
#
# resultado = minha_funcao(0)
#
# print(resultado)
#
# class Carro:
#     def __init__(self):
#         self.motor = 'desligado'
#         self.movimento = False
#
#     def ligar(self):
#         self.motor = 'ligado'
#
#     def acelerar(self):
#         if self.motor == 'ligado':
#             self.movimento = True
#
#     def carro_em_movimento(self):
#         return self.movimento
#
#
# carro = Carro()
# carro.acelerar()
# carro_em_movimento = carro.carro_em_movimento()
#
# print(carro_em_movimento)