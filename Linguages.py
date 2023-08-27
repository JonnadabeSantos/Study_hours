from time import sleep
from hours import *

linguages = {'Python': 0, 'Java Script': 0, 'ruby': 0,'Java': 0, 'C#': 0, 'SQL': 0, 'PHP': 0, 'C++': 0, 'Golang': 0 ,'CSS':0}
EndProgram = False



arq = 'Study_hours.txt'
if not verificarArquivo(arq):
    criarArquivo( arq, linguages)   
    registoGeral = arquivoExiste(arq)
    welcome = False
else:
    registoGeral = arquivoExiste(arq)
    welcome = True
   
if not welcome:
    cabeçalho('\033[33mWelcome Register your study hours here\033[m')
else:
    cabeçalho("\033[33mHi, it's good to have you here again.\033[m")

while True:
    
    if EndProgram:
        sair()
        break
    
    try:
        mainMenu = ['Add Hours','Statisc','Exit']
        menuList(mainMenu)        
        menuSelect = int(input(f'\nSelect Option: '))
    except:
        print('\n\033[31mERROR Select a valid option!\033[m')
        sleep(1)
    else:
        if menuSelect == 1:

            while True:
                menu( registoGeral )
                keylist = []
                for key in registoGeral.keys():
                    keylist.append(key)
                
                
                try :        
                    opc = int(input(f'Select Option: '))
                except:    
                    print('\033[31mERROR ! Digite um valor válido !!!\n\033[m')
                    sleep(1)
                else:    
                    if len( linguages ) + 2 >= opc > 0:
                        if opc == 1:
                            while True:
                                try:
                                    linha()
                                    cabeçalho('Python language selected !')
                                    resp = input(f'\nWant to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        print()                    
                                        print()                    
                                        cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies')
                                        for key, value in registoGeral.items():
                                            if key == keylist[ opc -1 ]:                                    
                                                print(f'{key:<33}{value} Hours')
                                        try:
                                            addhours = int(input('Enter the number of hours: '))
                                        except(ValueError):
                                            print('ERRO invalid Value !!')
                                        else:                                                
                                            registoGeral['Python'] = ( int(registoGeral['Python']) + addhours )
                                            # registoGeral['Python'] = int(registoGeral['Python']) + int(input('Enter the number of hours: '))
                                            updateDict( arq,registoGeral )
                                            print(f'Successfully adding {addhours} hours to your {keylist[ opc - 1 ]} studies')
                                            

                                    elif resp in 'Nn':                     
                                        break
                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                                
                                                
                        elif opc == 2:
                            cabeçalho(F'ADIÇÃO DE HORAS EM ')
                            nome = input('Nome-: ')
                            idade = int(input('Idade: '))
                            cadastrarNovo( arq, nome, idade )

                        elif opc == len( linguages ) + 1:
                            print('x')
                            break

                        elif opc == len( linguages ) + 2:
                            EndProgram = True                            
                            break
                        else:
                            print('e agora ?')
                    else:
                        print('\n\033[33mNúmero Inválido Type it again !!!\n\033[m')
                        sleep(1)
                
                
        
        elif menuSelect == 2:
            print('\nStatistic')
            sleep(1)
        
        elif menuSelect == 3:
            sair()
            break

        else:
            print('\nInvalid Number @@!!')
            sleep(1)

    



