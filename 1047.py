#horasIncial, horasFinal = map(int(input().split()))

horasIncial = int(input())
horasFinal = int(input())

def horas_jogando(horasInicial, horasFinal):
    if (horasIncial == horasFinal):
        print("O JOGO DUROU 24 HORA(S)")
    else:
        if horasInicial > horasFinal:
            aux = 24 - horasInicial
            horasTotal = aux + horasFinal
            print(f"O JOGO DUROU %d HORA(S)"%horasTotal)
        elif horasFinal > horasIncial:
            horasTotal = horasFinal - horasIncial
            print(f"O JOGO DUROU %d HORA(S)"%horasTotal)

horas_jogando(horasIncial, horasFinal)
