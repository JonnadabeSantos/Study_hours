from datetime import datetime, timedelta,time



def somar( fist, * number ):    
    for sun in number:
        fist += sun
    return fist


def subtract( fist, * number ):    
    for sub in number:
        fist -= sub
    return fist

def multiply( fist, * number ):  
    for mult in number:
        fist *= mult
    return fist


def division( fist, * number ):    
    for div in number:
        fist /= div
    return fist

def hourMinute( hour, minute ):
    # math.floor() arredonda p baixo
    #math.ceil() arredonda p cima
    hour += round( (minute / 60) , 1 )
    return hour


def studyTime( * lista ):
    hora = minuto = 0
    for item in lista:
        for ind, val in enumerate(item):
            if ind == 0:
                hora = val
            else:
                minuto = val

    print(f'A hora é {hora} e os minutos são {minuto}')
            

    
    # datet = datetime.strftime(now,'%H:%M')
    # now = timedelta(hours=1,minutes=5)

    # now = datetime.now()
    # periodo = ( now + timedelta( hours = int(input('Hour: ')), minutes = int(input('Minute: '))) ) - now
    # print(periodo)
    # print(now)

    ''' CONVERSÃO DE HORA E DATA

    today = datetime.now() + timedelta(hours=int(input('Houra: ')),minutes=int(input('Minutos: ')))
    htr = today.strftime('%H:%M')
    htr = today.strptime(htr, '%H:%M')
    print(type(htr))
    print(htr)

    htr =htr.strftime('%d/%b/%Y %H:%M') 
    print(type(htr))
    print(htr)

    htr = datetime.strptime(htr,'%d/%b/%Y %H:%M')
    print(type(htr))
    print(htr)
    '''
  


# print(type(studyTime()), studyTime())
# print(studyTime())
# studyTime()

a=20
b=2
c=3
d=4
e=5

# print(hourMinute(2,40))
