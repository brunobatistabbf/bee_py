#Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e 
# terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

#Entrada
#A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

#Saída
#Apresente a duração do jogo conforme exemplo abaixo.

#horasIncial, horasFinal = map(int(input().split()))

horasIncial = int(input())
horasFinal = int(input())

def horas_jogando(horaInicial, horaFinal):
    if (horasIncial == 0) and (horasFinal == 0):
        print("O JOGO DUROU 24 HORA(S)")
    pass 

horas_jogando(horasIncial, horasFinal)