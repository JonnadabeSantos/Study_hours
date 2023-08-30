from datetime import datetime, timedelta

# Crie um objeto timedelta com o intervalo de tempo desejado
intervalo_de_tempo = timedelta(days=0, hours=5, minutes=30)
print(intervalo_de_tempo)

# Crie um objeto datetime que servirá como ponto de partida
data_e_hora_partida = datetime(2023, 8, 29, 12, 0)  # Exemplo: 29 de agosto de 2023, 12:00

# Some o intervalo de tempo ao objeto datetime de partida para obter o resultado
data_e_hora_resultado = data_e_hora_partida + intervalo_de_tempo

# Agora, data_e_hora_resultado é um objeto datetime que representa a nova data e hora
print(data_e_hora_resultado)