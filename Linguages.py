from hours import *


arq = 'Study_hours.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
  
  

while True:
    menu( ['Python', 'Java_Script', 'Java', 'C#', 'Sair'] )
    opc = int(input(f'Selecione uma Opção: '))
    if 5 >= opc > 0:
        if opc == 1:
            lerArquivo(arq)
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
        
           

 



