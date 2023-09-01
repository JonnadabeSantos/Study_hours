def linha( aling = 40 ):
    print( '-' * aling )

def cabeçalho( txt, align = 40 ):
    linha(align)
    print(txt.center(align) )
    linha(align)


def menuList(lista):
    cabeçalho('Main Menu') 
    for ind, inf in enumerate(lista):
        print(f'{ ( ind + 1 ):>2} - {inf}')


def menu(dict):
    cabeçalho('Linguage Select')
    c = 1
    for key, value in dict.items():
        print(f'{c:>2} - {key:<24}{value:>8} Hours')
        c += 1
    print(f'{c:>} - Return to main menu')
    c += 1
    print(f'{c:>2} - Exit')    
    linha()

def cadastrar():
    print( '-' * 40 )
    print('OPÇÃO 01'.center(40) )
    print( '-' * 40 )

def dictr():
    print( '-' * 40 )
    print('OPÇÃO 02'.center(40) )
    print( '-' * 40 )

def sair():
    print( '-' * 40 )
    print('SAINDO ATE LOGO !'.center(40) )
    print( '-' * 40 )
