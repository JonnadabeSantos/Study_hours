from dados import *

def verificarArquivo(arquivo):
    try:        
        with open(arquivo, 'rt') as a: # 'rt vai ler um arquivo de texto 
            a.close() # fecha o arquivo
    except FileNotFoundError: # Arquivo não encontrado
        return False
    else:
        return True
    

def criarArquivo(nome,dici=''):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        try:
            a.write(f'{dici}')
        except:
            print('Houve um erro na escrita dos dados!')
        else:
            
            print(f'Arquivo  " {nome} " criado com sucesso!')
    finally:
        a.close()


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:     
        cabeçalho('Hours Studied')        
        for linha in a:            
            dado = linha.split(',')
               
        for limp in range(len(dado)):
            dado[limp] = dado[limp].replace("{","")
            dado[limp] = dado[limp].replace("}","")
            dado[limp] = dado[limp].replace("'","")
            dado[limp] = dado[limp].replace(" ","")
        
        registroGeral = {}  
        for separar in dado:
            keyValue = separar.split(':')
            registroGeral[keyValue[0]] = keyValue[1]                 
        
        print(registroGeral)    
    
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
