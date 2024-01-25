#Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
# A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
# sempre escrevendo uma mensagem adequada:
#se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
#se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
#se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
#se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
#se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
#Entrada
#A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

#Saída
#Imprima todas as classificações do triângulo especificado na entrada.
#a, b, c = map(float,input().split())

a = float(input())
b = float(input())
c = float(input())

lista_ordenada = [a, b, c]
lista_ordenada.sort(reverse=True)

def triangle_definition(lista_ordenada):
    a1 = lista_ordenada[0]
    b2 = lista_ordenada[1]
    c3 = lista_ordenada[2]
    if (a1 >= (b2 + c3)):
        print("NAO FORMA TRIANGULO")
    else:
        if((a1**2) == ((b2**2)+(c3**2))):
            print("TRIANGULO RETANGULO")
        if((a1**2) > ((b2**2)+(c3**2))):
            print("TRIANGULO OBTUSANGULO")
        if((a1**2) < (b2**2)+(c3**2)):
            print("TRIANGULO ACUTANGULO")
        if a1 == b2 == c3:
            print("TRIANGULO EQUILATERO")
        if (a1 == b2 != c3) or (a1 == c3 != b2) or (b2 == c3 != a1):
            print("TRIANGULO ISOSCELES")

if (a > 0) or (b > 0) or (c > 0):
    triangle_definition(lista_ordenada)
