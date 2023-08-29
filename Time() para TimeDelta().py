from datetime import datetime, time, timedelta

# Crie um objeto time com o tempo desejado
tempo = time(2, 30, 0)  # Exemplo: 2 horas, 30 minutos, 0 segundos

# Crie um objeto datetime com a data atual e o tempo desejado
data_atual = datetime.now().date()
data_e_tempo = datetime.combine(data_atual, tempo)

# Crie um objeto datetime com apenas a data
apenas_data = datetime(data_atual.year, data_atual.month, data_atual.day)

# Calcule a diferença entre os dois objetos datetime para obter um timedelta
diferenca = data_e_tempo - apenas_data

# A diferença agora é um objeto timedelta
print(diferenca)  # Isso imprimirá a diferença entre o tempo especificado e a meia-noite de hoje
