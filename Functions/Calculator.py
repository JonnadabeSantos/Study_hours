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
            
    
def studyTime( fist, second, lista ):
    fistHora = fistMinuto = dia = 0
    separar = lista.split(':')
      
    for ind, horaMinuto in enumerate(separar):
        horaMinuto = int(horaMinuto)        
        if ind == 0:
            while horaMinuto >= 24:
                dia += 1
                horaMinuto -= 24
            fistHora = horaMinuto
        else:
            fistMinuto = horaMinuto
   
    tempo = timedelta( days = dia, hours = fistHora, minutes = fistMinuto )
    tempo += timedelta( hours = fist, minutes = second )
    dia = tempo.days
     
    data = datetime.now().date()
    resettime = time(0,0)
    data = datetime.combine( data, resettime )
 
    data += tempo
    Hora = data.hour + ( dia * 24 )
    Minuto = data.minute
    
    if Minuto == 0:
        return f'{Hora}'
    
    else:
        return f'{Hora}:{Minuto}'
 



    # horaMinuto = hourMinute( fist, second, hora, minuto )

    # return f'{horaMinuto[0]}:{horaMinuto[1]}'


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
