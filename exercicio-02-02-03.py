"""
    Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
    então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo
    usado em primeiro lugar, que horas chego em casa para o café da manhã?
    R. Hora de chegada: 07:30:06
"""


def hms(segundos):
    hora = segundos // 3600
    segundos -= (hora * 3600)
    minuto = segundos // 60
    segundo = segundos % 60
    return hora, minuto, segundo


def main():
    inicio = (6 * 3600) + (52 * 60)
    h, m, s = hms(inicio)
    print(f'Hora de Início: {h:0>2d}:{m:0>2d}:{s:0>2d}')

    corrida = ((8 * 60 + 15) * 2) + ((7 * 60 + 12) * 3)
    h, m, s = hms(corrida)
    print(f'Tempo de Corrida: {h:0>2d}:{m:0>2d}:{s:0>2d}')

    chegada = inicio + corrida
    h, m, s = hms(chegada)
    print(f'Hora de chegada: {h:0>2d}:{m:0>2d}:{s:0>2d}')


if __name__ == '__main__':
    main()
