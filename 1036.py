#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.

#Entrada
#Leia três valores de ponto flutuante (double) A, B e C.

#Saída
#Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
# Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, 
# com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.


import math
from flask.scaffold import F


a = float(input())
b = float(input())
c = float(input())


def bhaskara(a, b, c):
    delta = (b**2) - (4 * (a * c))
    if a == 0:
        print("Impossivel Calcular")
    else:
        x1 = (- b + math.sqrt(delta))/(2 * a)
        x2 = (- b - math.sqrt(delta))/(2 * a)
        if (x1<=0) or (x2<=0) or (a==0):
            print("Impossivel Calcular")
        else:
            return x1, x2

    if (x1<=0) or (x2<=0) or (a==0):
        print("Impossivel Calcular")
    else:
        return x1, x2
    

x1, x2 = bhaskara(a, b, c)
print(f"R1 = {x1:.5f}")
print(f"R2 = {x2:.5f}")