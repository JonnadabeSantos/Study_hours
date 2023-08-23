from dados import *

def arquivoExiste(arquivo):
    try:        
        with open(arquivo, 'rt') as a: # 'rt vai ler um arquivo de texto 
            a.close() # fecha o arquivo
    except FileNotFoundError: # Arquivo não encontrado
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo  " {nome} " criado com sucesso!')
    finally:
        a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('Hours Studied')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace( '\n' , '' ) # isso vai remover a quebra de linha
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrarNovo( arq, nome='desconhecido', idade=0 ):
    try:
        a = open( arq, 'at')
    except:
        print('houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escrita dos dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
