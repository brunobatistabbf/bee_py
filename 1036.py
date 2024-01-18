#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.

#Entrada
#Leia três valores de ponto flutuante (double) A, B e C.

#Saída
#Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
# Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, 
# com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

#a, b, c = map(float, input().split())

import math

a = float(input())
b = float(input())
c = float(input())


def bhaskara(a, b, c):
    
    delta = (b**2) - (4 * (a * c))
    
    if (a == 0) or (delta < 0):
        return None
    else:
        x1 = (- b + math.sqrt(delta))/(2 * a)
        x2 = (- b - math.sqrt(delta))/(2 * a)
        return x1, x2
        
resultado = bhaskara(a,b,c)

if resultado is None:
    print("Impossivel calcular")
else:
    x1, x2 = resultado
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")