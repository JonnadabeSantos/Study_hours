from hours import *


arq = 'Exercise\My_Exercice\Study_hours.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
  
  

while True:
    menudict( {'Python':'0', 'Java_Script':'0', 'Java':'0', 'C#':'0', 'Sair':'0'} )
    opc = int(input(f'Selecione uma Opção: '))
    if 5 >= opc > 0:
        if opc == 1:
            lerArquivo(arq)
                
        elif opc == 2:
            cabeçalho(F'ADIÇÃO DE HORAS EM ')
            nome = input('Nome-: ')
            idade = int(input('Idade: '))
            cadastrarNovo( arq, nome, idade )

        elif opc == 5:
            sair()
            break
        else:
            print('\033[31m ERROR ! Digite um valor válido !\033[m')
        
           

 



