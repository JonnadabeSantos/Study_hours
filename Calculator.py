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


a=20
b=2
c=3
d=4
e=5

print(hourMinute(2,40))
