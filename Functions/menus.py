def linha( aling=45 ):
    return ('-' * aling )

def cabeçalho( txt, align=45 , line = 'both' ):
    cab = f'{ txt.center(align) }'
    
    if line == 'top':
        return f'{linha()}\n{cab}'
    
    elif line == 'bottom':
        return f'{cab}\n{linha()}'

    elif line == 'both':
        return f'{linha()}\n{cab}\n{linha()}\n'
    
    elif line == None:
        return cab



def menuList(lista):    
    for ind, inf in enumerate(lista):
        print(f'{ ( ind + 1 ):>2} - {inf}')


def menu(dict):    
    c = 1
    for key, value in dict.items():
        print(f'{c:>2} - {key:<24}{value:>8} Hours')
        c += 1
    print(f'{c:>} - Return to main menu')
    c += 1
    print(f'{c:>2} - Exit')    
    print(linha())

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
