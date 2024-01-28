#horasInicial, minutosInicial, horasFinal, minutosFinal = map(int(input().split()))

horasInicial = int(input())
minutosInicial = int(input())
horasFinal = int(input())
minutosFinal = int(input())


def horas_jogando(horasInicial,minutosInicial, horasFinal,minutosFinal):
    diferenca = (((horasFinal * 60) + minutosFinal) - ((horasInicial * 60) + minutosInicial))
    if diferenca <= 0:
        diferenca += 24*60
    
    horas = diferenca // 60
    minutos = diferenca % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
        
horas_jogando(horasInicial,minutosInicial, horasFinal,minutosFinal)