from hours import *

linguages = {'Python': 0, 'Java Script': 0, 'Ruby':0, 'Java': 0, 'C#': 0, 'SQL': 0, 'PHP': 0, 'C++': 0, 'Golang': 0}



arq = 'Study_hours.txt'
if not verificarArquivo(arq):
    criarArquivo( arq, linguages)
else:
    arquivoExiste(arq)

  
  

while True:
    menu( linguages )
    opc = int(input(f'Selecione uma Opção: '))
    if 5 >= opc > 0:
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

        if opc == 5:
            sair()
            break
        else:
            print('\033[31m ERROR ! Digite um valor válido !\033[m')
        
           

 



