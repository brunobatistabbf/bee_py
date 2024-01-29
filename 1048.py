#Entrada
#A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

#Saída
#Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
#(ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

#salario= map(int,float().split()))

salario = float(input())
#salario_formatado = round(salario, 2)
print(salario)
def calculo_salario(salario):
    if salario >= 0 and salario <= 400 :
        reajuste =+ salario * 0.15
        salario_reajustado = salario + reajuste
        percentual = 15
        print(f"Novo salario: {salario_reajustado}")
        print(f"Reajuste ganho: {reajuste}")
        print(f"Em percentual: {percentual} %")
        
    return 0

calculo_salario(salario)