
lista = [1,10]

try:
    divisao = 10/1
    numero = lista[1]
    x=a
except ZeroDivisionError:
    print('nao divide zero')
except IndexError:
    print('erro indice')
except BaseException as ex:
    print('erro desconhecido: {} '.format(ex))
# except
#     print('erro qualquer')

