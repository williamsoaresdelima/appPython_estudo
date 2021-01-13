# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
#
# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)
#
# soma=0
# for x in lista:
#     soma += x
# print(soma)
#
# print(max(lista_animal))
#
# if 'gatolindo' in lista_animal:
#     print('tem')
# else:
#     lista_animal.append('gatolindo')
#     print(lista_animal)
#
# lista_animal.pop(2);
# print(lista_animal)

# nova_lista = lista_animal *3
# print(nova_lista)

#
# lista_animal.remove('elefante');
# print(lista_animal)
#
# lista.sort()
# print(lista)
#
# lista.reverse()
# print(lista)
#
# tupla = (1,2,3,5,12,15)
#
# print(len(tupla))
#
# tupla_animal=tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)
#
# listanumerica = list(tupla_animal)
# print(listanumerica)


lista = [1, 3, 2, 4]
lista.sort()
lista.reverse()
print(lista)

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)

