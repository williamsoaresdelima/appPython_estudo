conjunto = {1,2,3,4}
print(conjunto)

conjunto.add(5)
conjunto.discard(3)
print(conjunto)

conjunto2={4,5,6,7,8}

conjunto_uniao =conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)

conjunto_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_simetrica)


#subset - se um conjunto é um subconjunto do 2
conjunto_a={1,2,3}
conjunto_b={1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista =['gato','gato','cachorro','Elefante']
print(lista)

conjunto_animais = set(lista)
print(conjunto_animais)

lista = list(conjunto_animais)
print(lista)


conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)


mariana = 2 # dona da casa
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
participantes = len(dedos) #quantidade de participantes
somaDedos = sum(dedos) #soma dos valores de cada dedo
dedoapontadopara = 0
for x in range(somaDedos):
  if dedoapontadopara > participantes:
     dedoapontadopara = 0
  dedoapontadopara += 1
dedos = list(dedos) #converter dedos para arquivo tipo 'list'
print('No final o dedo foi apontado para {}.'.format(dedos[dedoapontadopara]))

conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}

conjunt_u = conjunto1.union(conjunto2)
print(conjunt_u)

conjunto = {10, 20, 30, 40, 50}
conjunto.discard (40)

print(conjunto)

conjunto = {1, 2, 2, 1, 4, 5}
print(conjunto)