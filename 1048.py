#Entrada
#A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

#Saída
#Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
#(ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

#salario = map(int,float().split())

salario = float(input())
#salario = round(salario_informatado, 2)

def calculo_salario(salario):
    if (salario >= 0 and salario <= 400.00):
        reajuste =+ salario * 0.15
        salario_reajustado = salario + reajuste
        percentual = 15
        print(f"Novo salario: {salario_reajustado:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual} %")
  
    elif (salario>= 400.01 and salario <= 800.00):
        reajuste =+ salario * 0.12
        salario_reajustado = salario + reajuste
        percentual = 12
        print(f"Novo salario: {salario_reajustado:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual} %")
  
    elif (salario>= 800.01 and salario <= 1200.00):
        reajuste =+ salario * 0.10
        salario_reajustado = salario + reajuste
        percentual = 10
        print(f"Novo salario: {salario_reajustado:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual} %")
  
    elif (salario>= 1200.01 and salario <= 2000.00):
        reajuste =+ salario * 0.07
        salario_reajustado = salario + reajuste
        percentual = 7
        print(f"Novo salario: {salario_reajustado:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual} %")
  
    elif (salario > 2000.00):
        reajuste =+ salario * 0.04
        salario_reajustado = salario + reajuste
        percentual = 4
        print(f"Novo salario: {salario_reajustado:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual} %")
    
    else:
        print("Insira um valor valido.")

calculo_salario(salario)