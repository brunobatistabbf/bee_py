# -*- coding: utf-8 -*-

valor = float(input())

notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
quantidade_notas_e_moedas = {}


for nota_moeda in notas_moedas:
    quantidade = int(valor//nota_moeda)
    valor %= nota_moeda
    quantidade_notas_e_moedas[nota_moeda] = quantidade
    
print("NOTAS:")
for nota in [100, 50, 20, 10, 5, 2, 1]:
    print(f"{quantidade_notas_e_moedas[nota]} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda in [0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f"{quantidade_notas_e_moedas[moeda]} moeda(s) de R$ {moeda:.2f}")
    
#terminar depois
