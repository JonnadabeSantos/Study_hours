from Functions.Calculator import *
from Functions.menus import *

def verificarArquivo(arquivo):
    try:        
        with open(arquivo, 'rt') as a: # 'rt vai ler um arquivo de texto 
            a.close() # fecha o arquivo
    except FileNotFoundError: # Arquivo não encontrado
        return False
    else:
        return True
 

def criarArquivo(nome,dici):
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
        for linha in a:            
            dado = linha.split("',")
               
        for limp in range(len(dado)):
            dado[limp] = dado[limp].replace("{","")
            dado[limp] = dado[limp].replace("}","")
            dado[limp] = dado[limp].replace("'","")
            dado[limp] = dado[limp].replace(" ","")

        registroGeral = {}  

        for separar in dado:
            keyValue = separar.split(':')
            
            if len(keyValue) == 3:
                registroGeral[keyValue[0]] = f'{keyValue[1]}:{keyValue[2]}'
            else:
                registroGeral[keyValue[0]] = f'{keyValue[1]}'
        
        a.close()
        return registroGeral  


def updateDict( arq, dict ):
    try:
        a = open( arq, 'wt+')
    except:
        print('Houve um erro na abertura dos dados!')
    else:
        try:
            a.write(f'{dict}' )
            a.close()
        except:
            print('Houve um erro na escrita dos dados!')

    

def updateHours( arq, addDate ):
    try:
        a = open( arq, 'at')
    except:
        print('Houve um erro na abertura dos dados!')
    else:
        try:
            a.write(f'{addDate}\n' )
        except:
            print('Houve um erro na escrita dos dados!')
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


def register_hours( hour, minute, hourMinute, data = False ):    
    dateNow = datetime.now().strftime('%d/%m/%Y')

    if ( hour and minute ) != 0:
        if data:
            string_horaMinuto = f'{hour:>2} hour(s) and {minute:>2} minute(s)'
            string_timestudy = f'your current study time is {hourMinute} Hour(s)'
            return f'{dateNow} - added  {string_horaMinuto:<28} -  {string_timestudy:<41}'
        else:
            return f'Successfully adding {hour} hour(s) and {minute} minute(s) to your -'
    
    else:   
        if hour == 0 and minute != 0:
            if data:
                string_minute = f'{minute:>2} minute(s)'
                string_time = f'your current study time is {hourMinute} Hour(s)'
                return f'{dateNow} - added  {string_minute:>27}  -  {string_time:<41}'
            else:
                return f'Successfully adding {minute} minute(s) to your -'

        elif hour != 0 and minute == 0:
            if data:
                string_hour = f'{hour:>2} hour(s)'
                string_Fulltime = f'your current study time is {hourMinute} Hour(s)'
                return f'{dateNow} - added  {string_hour:<29}-  {string_Fulltime:<41}'
            else:
                return f'Successfully adding {hour} hour(s) to your -'
        else:
            return f'Sorry ! but no hour(s) or minute(s) was added to your -'
