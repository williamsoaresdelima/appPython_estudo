# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print('meu app')
a = int(input('Digite 1: '))
b = int(input('Digite 2: '))

soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
resto=a%b

print(type(soma))
print('soma {so} .\nsubtracao {sub}' .format(so=soma, sub=subtracao))

c = int(input('Primeiro Valor: '))
d = int(input('Segundo Valor: '))
e = int(input('Segundo Valor: '))

if c> d and c > e:
    print ('maior numro é {}'.format(c))
elif d > c and d > e:
    print('o maior numero é {}'. format(d))
else:
    print('o maior numero é {}'.format(e))
print ('final prog')

mod = c%2

if mod==0:
    print('par')
else:
    print ('impar')