"""
    Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio
    (tempo por milha em minutos e segundos)?
    Qual é a sua velocidade média em milhas por hora?
    R. 22.62295 mph
"""

distancia_milha = 10 * 1.61
tempo_horas = ((42 * 60) + 42)/3600
velocidade_mph = round(distancia_milha / tempo_horas, 5)
print(velocidade_mph)
