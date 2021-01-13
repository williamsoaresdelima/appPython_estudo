
def escrever_arquivo(texto):
    arquivo = open('aluno.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')

    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
        print(media(lista_notas))
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'C:/projetos/pythonFundamentos/')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,'C:/projetos/pythonFundamentos/')

#
# lista_media = media_notas('notas.txt')
# print(lista_media)
#
# move_arquivo('notas.txt')
#
# aluno='Cezar,10,10,6,7\n'
# atualizar_arquivo('notas.txt',aluno)
# ler_arquivo('notas.txt')

# escrever_arquivo('primeira linha\n')
# atualizar_arquivo('segunda linha\n')
# ler_arquivo('teste.txt')

resultado = 'João programa em Python, Java, PHP e Ruby'.split('*')
print(resultado)


