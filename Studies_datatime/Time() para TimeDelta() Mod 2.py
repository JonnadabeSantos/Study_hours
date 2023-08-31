from datetime import datetime, time

print()
here = datetime(2035,6,13)
print(type(here))
print(here)

hora = time(14,30)
print(hora)
print()

mixer = datetime.combine(here,hora)
print(mixer)
print(type(mixer))

print()
data_agora = datetime.now().date()
hora_agora = datetime.now().time()

print(data_agora)
print(type(data_agora))

print()
print(hora_agora)
print(type(hora_agora))
print()

novoMixer = datetime.combine(data_agora,hora_agora)
print(novoMixer)