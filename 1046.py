#Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e 
# terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

#Entrada
#A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

#Saída
#Apresente a duração do jogo conforme exemplo abaixo.

#horasIncial, horasFinal = map(int(input().split()))

horasIncial = int(input())
horasFinal = int(input())

def horas_jogando(horasInicial, horasFinal):
    if (horasIncial == 0) and (horasFinal == 0):
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
