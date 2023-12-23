def linha( aling = 45 ):
    return ('-' * aling )

def cabeçalho( txt, linhaCab = 45 , line = 'both' ):
    cab = f'{ txt.center(linhaCab) }'
    
    if line == 'top':
        return f'{linha(linhaCab)}\n{cab}'
    
    elif line == 'bottom':
        return f'{cab}\n{linha(linhaCab)}'

    elif line == 'both':
        return f'{linha(linhaCab)}\n{cab}\n{linha(linhaCab)}\n'
    
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
    print('OPTION 01'.center(40) )
    print( '-' * 40 )

def dictr():
    print( '-' * 40 )
    print('OPTION 02'.center(40) )
    print( '-' * 40 )

def sair():
    print( '-' * 40 )
    print('see you soon !'.center(40) .upper() )
    print( '-' * 40 )
