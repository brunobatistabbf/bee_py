#Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.
#Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.
#Entrada
#Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. 
# Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss.
# Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das 
# duas primeiras linhas, indicando o término do evento.
#Saída
#Na saída, deve ser apresentada a duração do evento, no seguinte formato:
#W dia(s)
#X hora(s)
#Y minuto(s)
#Z segundo(s)
#Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

#parte inicial
dia_word_string, dia_number_string = list(input().split(" "))
dia_number =  int(dia_number_string)
horas, minutos, segundos = list(input().split(" : "))
horas_number = int(horas)
minutos_number = int(minutos)
segundos_number = int(segundos)

#parte final
dia_word_string_final, dia_number_string_final = list(input().split(" "))
dia_number_final =  int(dia_number_string_final)
horasf, minutosf, segundosf = list(input().split(" : "))
horas_numberf = int(horasf)
minutos_numberf = int(minutosf)
segundos_numberf = int(segundosf)

def calcular_evento_tempo(dia_number, horas_number, minutos_number, segundos_number, dia_number_final, horas_numberf, minutos_numberf, segundos_numberf):
    if horas_numberf < horas_number:
        dia = dia_number_final - dia_number - 1
    else:
        dia = dia_number_final - dia_number

    hora = (horas_numberf - horas_number) % 24

    
    if hora < 0:
        hora = hora + 24
        dia = dia - 1
    minuto = minutos_numberf - minutos_number
    
    if minuto < 0:
        minuto = minuto + 60
        hora = hora - 1
    segundos = segundos_numberf - segundos_number
    
    if segundos < 0:
        segundos = segundos + 60
        minuto = minuto - 1
        
    if dia < 0:
        dia = 0 
        
    print(f"{dia} dia(s)")
    print(f"{hora} hora(s)")
    print(f"{minuto} minuto(s)")
    print(f"{segundos} segundo(s)")


calcular_evento_tempo(dia_number, horas_number, minutos_number, segundos_number, dia_number_final, horas_numberf, minutos_numberf, segundos_numberf)

