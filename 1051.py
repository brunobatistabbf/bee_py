salario = (float( input()))

def imposto_de_renda(salario):
    try:
        if (salario >= 0) and (salario <= 2000):
            print("Isento")
        elif (salario >= 2000.01) and (salario <= 3000):
            reajuste =+ salario * 0.08
            print(f"R$ {reajuste:.2f}")
        elif (salario >= 3000.01 ) and (salario <= 4500):
            reajuste =+ salario * 0.18
            print(f"R$ {reajuste:.2f}")
    except:
        print("Insira um valor válido!")
        return 0

imposto_de_renda(salario)