from time import sleep
from hours import *

linguages = {'Python': 0, 'Java Script': 0, 'ruby': 0,'Java': 0, 'C#': 0, 'SQL': 0, 'PHP': 0, 'C++': 0, 'Golang': 0}



arq = 'Study_hours.txt'
if not verificarArquivo(arq):
    criarArquivo( arq, linguages)   
    registoGeral = arquivoExiste(arq)
else:
    registoGeral = arquivoExiste(arq)
   

while True:
    menu( registoGeral )
    try :
        opc = int(input(f'Select Option: '))
        
        if len( linguages ) + 1 >= opc > 0:
            if opc == 1:           
                while True:
                    resp = input('Return to menu [Y/N]?: ') [0]
                    if resp in 'Yy':                    
                        break
                    elif resp in 'Nn':
                        opc = 5
                        break
                    else:
                        print('\033[31mERROR ! Type YES or NO \033[m')
                

            if opc == 2:
                cabeçalho(F'ADIÇÃO DE HORAS EM ')
                nome = input('Nome-: ')
                idade = int(input('Idade: '))
                cadastrarNovo( arq, nome, idade )

            if opc == len( linguages ) + 1:
                sair()
                break
        else:
            print('\033[33mNúmero Inválido !!!\n\033[m')
            sleep(1)
    
    except:    
        print('\033[31mERROR ! Digite um valor válido !\n\033[m')
        sleep(1)
        
           

 



