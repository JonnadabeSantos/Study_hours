from time import sleep
from hours import *

linguages = {'Python': 0, 'Java Script': 0, 'ruby': 0,'Java': 0, 'C#': 0, 'SQL': 0, 'PHP': 0, 'C++': 0, 'Golang': 0 ,'CSS':0}



arq = 'Study_hours.txt'
if not verificarArquivo(arq):
    criarArquivo( arq, linguages)   
    registoGeral = arquivoExiste(arq)
    welcome = False
else:
    registoGeral = arquivoExiste(arq)
    welcome = True
   

while True:
    print()
    keylist = []
    mainMenu = ['Add Hours','Statisc','Exit']
        
    if not welcome:
        cabeçalho('\033[33mWelcome Register your study hours here\033[m')
    else:
        cabeçalho("\033[33mHi, it's good to have you here again.\033[m")
    menuList(mainMenu)
    opc = int(input(f'\nSelect Option: '))


    menu( registoGeral )
    for key in registoGeral.keys():
        keylist.append(key)
    
    
    try :        
        opc = int(input(f'Select Option: '))
        
        if len( linguages ) + 1 >= opc > 0:
            if opc == 1:
                linha()
                cabeçalho('Python language selected !')
                while True:
                    try:
                        resp = input(f'\nWant to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]            
                        if resp in 'Yy':
                            print()                    
                            print()                    
                            cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies')
                            for key, value in registoGeral.items():
                                if key == keylist[ opc -1 ]:                                    
                                    print(f'{key:<33}{value} Hours')                               
                            addhours = int(input('Enter the number of hours: '))
                            registoGeral['Python'] = ( int(registoGeral['Python']) + addhours )
                            # registoGeral['Python'] = int(registoGeral['Python']) + int(input('Enter the number of hours: '))
                            updateDict( arq,registoGeral )
                            print(f'Successfully adding {addhours} hours to your {keylist[ opc - 1 ]} studies')
                            

                        elif resp in 'Nn':                     
                            break
                        else:
                            print('\nIvalid Option ! Type YES or NO')
                            sleep(1)

                    except:
                        print('\033[31m\nERROR ! Invalid value \033[m')
                        sleep(1)
                                     
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
        
           

 



