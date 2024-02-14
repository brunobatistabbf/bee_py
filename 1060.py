#Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
#A seguir, mostre a quantidade de valores positivos digitados.

#Entrada
#Seis valores, negativos e/ou positivos.

#Saída
#Imprima uma mensagem dizendo quantos valores positivos foram lidos.

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

valores = a, b, c, d, e, f

def valores_positivos(valores):
    valores_positivos = 0
    
    for numero in valores:
        if numero > 0:
            valores_positivos =+ valores_positivos + 1
            
    print(f"{valores_positivos} valores positivos")

valores_positivos(valores)