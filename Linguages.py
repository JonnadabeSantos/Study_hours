from Functions.main_functions import *
from time import sleep

linguages = {'Python': '0', 'Java Script': '0', 'Java': '0', 'C#': '0', 'C++': '0', 'SQL': '0', 'PHP': '0', 'Typescript': '0', 'Golang': '0', }
EndProgram = returnMainMenu = False



arq = 'Fake_bank/Study_hours.txt'
if not verificarArquivo(arq):
    criarArquivo( arq, linguages)   
    registoGeral = arquivoExiste(arq)
    welcome = False
else:
    registoGeral = arquivoExiste(arq)
    welcome = True
   
if not welcome:
    print(cabeçalho('\033[33mWelcome Register your study hours here\033[m', 52, 'top' ))
else:
    print(cabeçalho("\033[33mHi, it's good to have you here again.\033[m", 54, 'top' ))



while True:
    
    if EndProgram:
        print()
        sair()
        break
    
    try:
        mainMenu = ['Add Hours','Statisc','Exit']
        print(cabeçalho('Main Menu') )
        menuList(mainMenu)        
        menuSelect = int(input(f'\nSelect Option: '))
    except:
        print('\n\033[31mERROR Select a valid option!\033[m')
        sleep(1)
    else:

        if menuSelect == 1:

            while True:
                
                returnMainMenu = False
                if EndProgram:                    
                    break
              
                print(cabeçalho('Linguage Select'))
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
                        
                        if opc == 1: # Python
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 110 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                                
                                                
                        
                       
                       
                        elif opc == 2:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 114 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                                



                        elif opc == 3:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 108 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                                                           
                
                
                        
                        
                        elif opc == 4:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 106 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                              
        
                        elif opc == 5:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 107 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)                              




                        elif opc == 7:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 107 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)       





                        elif opc == 5:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 107 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)       




                        elif opc == 8:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 114 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)   




                        elif opc == 9:
                            
                            while True:
                                
                                if EndProgram or returnMainMenu:
                                    break

                                try:
                                    print(cabeçalho(f'{keylist[ opc -1 ]} language selected !'))
                                    resp = input(f'Want to add hours {keylist[ opc -1 ]} language? [Y/N]?: ') [0]
                                except:
                                    print('\n\033[31m\nERROR ! Invalid value \033[m')
                                    sleep(1)
                                else:
                                    if resp in 'Yy':
                                        while True:

                                            if EndProgram or returnMainMenu:
                                                break

                                            print()                    
                                            print()                    
                                            print(cabeçalho(f'Adding hours to {keylist[ opc -1 ]} studies'))
                                            for key, value in registoGeral.items():
                                                if key == keylist[ opc -1 ]:                                    
                                                    print(f'{key:<33}{value} Hours')
                                            try:
                                                addhours = int(input('Enter the number of hours: '))
                                                addminite = int(input('Enter the number of minutes: '))
                                                addTime = studyTime( addhours, addminite, registoGeral[keylist[ opc - 1] ])

                                            except(ValueError):
                                                print('\n\033[31m\nERROR ! Invalid value*** \033[m')
                                                sleep(1)
                                            else:                                                
                                                print( f'{register_hours( addhours, addminite, addTime )} {keylist[ opc - 1 ]} studies' )
                                                reg_now = f'{register_hours( addhours, addminite, addTime, True )} - {keylist[ opc - 1 ]} studies'

                                                registoGeral[ keylist[ opc -1 ] ] = addTime
                                                updateDict( arq,registoGeral )

                                                file_linguage = f'Fake_bank/Hours_linguages/{keylist[ opc - 1]}.txt'                                            
                                                if not verificarArquivo(file_linguage) and ( addhours or addminite ) != 0:                                                 
                                                    criarArquivo( file_linguage, cabeçalho( f"{keylist[ opc - 1]} language time recording", 110 ) )                                                                                                 
                                                    updateHours( file_linguage, reg_now )
                                               
                                                else:
                                                    if not 'Sorry' in reg_now:                                                 
                                                        updateHours( file_linguage, reg_now )
                                                        
                                                

                                                while True:                     
                                                    try:
                                                        returned = input('\nReturn to main menu [Y/N]: ') [0]
                                                    except:
                                                        print('\033[31m\nERROR ! Invalid value \033[m')
                                                    else:
                                                        if returned in 'Yy':
                                                            returnMainMenu = True
                                                            break
                                                        elif returned in 'Nn':

                                                            EndProgram = True # used to end all whiles
                                                            break
                                                        else:
                                                            print('\nIvalid Option ! Type YES or NO')
                                                            sleep(1)                                              
                                                                                               

                                    elif resp in 'Nn':
                                        while True:                     
                                            try:
                                                returned = input('Return to main menu [Y/N]: ') [0]
                                            except:
                                                print('\033[31m\nERROR ! Invalid value \033[m')
                                            else:
                                                if returned in 'Yy':
                                                    returnMainMenu = True
                                                    break
                                                elif returned in 'Nn':

                                                    EndProgram = True # used to end all whiles
                                                    break
                                                else:
                                                    print('\nIvalid Option ! Type YES or NO')
                                                    sleep(1)                                                   

                                    else:
                                        print('\nIvalid Option ! Type YES or NO')
                                        sleep(1)       
                        
                        elif opc == len( linguages ) + 1:
                            break

                        elif opc == len( linguages ) + 2:
                            EndProgram = True

                    else:
                        print(f'ERROR ! select number between 1 and {len( linguages ) + 2}\n')
                        sleep(1)







        elif menuSelect == 2:
            print('\nStatistic')
            sleep(1)
        
        elif menuSelect == 3:
            EndProgram = True            

        else:
            print(f'\n\033[33mInvalid Number !! a number between 1 and { len(mainMenu) }\n\033[m')
            sleep(2)



