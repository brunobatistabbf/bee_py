#Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média 
# de todos os valores positivos digitados, com um dígito após o ponto decimal.

#Entrada
#A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

#Saída
#O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

def valores_positivos(a, b, c, d, e, f):
    quantidade_positivos = 0
    aux = 0
    if (a and b and c and d and e and f) < (0):
        return 0
    
    for numero in a, b, c, d, e, f:
        if numero > 0:
            quantidade_positivos += 1
            aux = numero + aux

    media = aux/quantidade_positivos    
    
    print(f"{quantidade_positivos} valores positivos")
    print(f"{media:.1f}")        
    
    
    
valores_positivos(a, b, c, d, e, f)