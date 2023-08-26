def linha():
    print( '-' * 40 )

def cabeçalho( txt ):
    linha()
    print(txt.center(40) )
    linha()

def menu(dict):
    cabeçalho('Main Menu')
    c = 1
    for key, value in dict.items():
        print(f'{c:>2} - {key:<24}{value:>4} Hours')
        c += 1
    print(f'{c:>2} - Sair')    
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
