# Parametro 'w' reescreve tudo, parametro 'a' atualiza, preservando o restante

import shutil

def escrever_arquivo(texto):
    diretorio = 'D:/ju/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo  = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # parametro 'r' -> Read -> abrir pra leitura
    texto = arquivo.read()
    #print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
   # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media


def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/ju/')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/ju/')


if __name__ == '__main__':
    mover_arquivo('teste.txt')
    #copiar_arquivo('media.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha\n')
    #aluno = 'Cesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
