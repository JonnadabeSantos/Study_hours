from dados import *

def arquivoExiste(arquivo):
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


# def arquivoExiste(nome):
#     try:
#         a = open(nome, 'rt')
#     except:
#         print('houve um ERRO na existência do arquivo!')
#     else:
#         a.write()



def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(f'{a} #')
        cabeçalho('Hours Studied')        
        for linha in a:            
            dado = linha.split(',')
        
        print(dado)
        for limp in range(len(dado)):
            dado[limp] = dado[limp].replace("{","")
            dado[limp] = dado[limp].replace("}","")
            dado[limp] = dado[limp].replace("'","")
            dado[limp] = dado[limp].replace(" ","")
        
    

        for ver in dado:
            print(f'{ver}')
        print(dado)
        k = []
        v = []
        for sep in dado:
            final = sep.split(':')
            k.append(final)
           
        print()  
        print(dado)  
        print()  
        print(k)
        print(v)
        dc = {}  
        for x, z in enumerate(k):              
            dc[z[0]] = z[1]

        
        
        print(dc)
        print(dc['Python'])
        print(dc['C++'])
        print(dc['Java'])

            
                 

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
