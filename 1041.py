#Calculo do quadrante das coordenadas em um plano cartesiano
#a, b = map(float,input().split())
a = float(input())
b = float(input())

x = round(a, 2)
y = round(b, 2)

if x == 0 and y == 0:
    print("Origem")
elif x==0:
    print("Eixo Y")
elif y==0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Entrada Inválida")