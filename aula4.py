# a = int(input('primeiro valor '))
# b = int(input('segundo valor '))
# c = int(input('terceiro valor '))
#
#
# if a>b:
#     print('o maior numero {}'.format(a))
# elif b> a and b> c:
#     print('o maior numero {}'.format(b))
# else:
#     print('o maior numero {}'.format(c))

# a=int(input('digite um numero '))
# b=int(input('digite outro numero '))
# resto_a = a%2
# resto_b = b%2
#
# if resto_a==0 or resto_b==0:
#     print('numero par digitado')
# else:
#     print('sem numero par')

#
# a = int(input('Primeiro Bimestr '))
# b = int(input('Segundo Bimestr '))
# c = int(input('Terceiro Bimestr '))
# d = int(input('Quarto Bimestr '))
#
# media = (a+b+c+d)/4
#
# if a<=10 and b<=10 and c<=10 and d<=10:
#     print('Media: {}'.format(media))
# else:
#     print('Nota Errada Inserida')

#
# a = int(input('Primeiro Bimestr '))
# b = int(input('Segundo Bimestr '))
# c = int(input('Terceiro Bimestr '))
# d = int(input('Quarto Bimestr '))
#
# media = (a + b + c + d) / 4
#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media: {}'.format(media))
# else:
# #     print('Nota Errada Inserida')
#
# a = 10
# b = 10
# c = 10
# if a > b or a >= c:
#     print('Primeiro afirmação é verdadeira')
# elif a == b:
#     print('Segunda afirmação é verdadeira')
# else:
#     print('Nenhuma afirmação é verdadeira')
#
#
# if not 5==5:
#     print('afirmação verdadeira')
# else:
#     print('afirmação falsa')
#
# a = input('Digite o primeito valor: ')
# b = input('Digite o primeito valor: ')
# soma = a + b
# print('O valor da soma é: {soma}'.format(soma=soma))



a = 0
resultado = 'neutro'
if a > 0:
    resultado = 'positivo'
elif a < 0:
    resultado = 'negativo'
a = resultado

print(resultado)
