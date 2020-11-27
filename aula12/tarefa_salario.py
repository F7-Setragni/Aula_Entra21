dinheiro_horas = float(input('Quanto você recebe por hora?: '))
horas_mes = float(input('Por quantas horas por mês?: '))
salario_bruto = dinheiro_horas * horas_mes
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario = salario_bruto - (imposto_de_renda + inss + sindicato)

print(f'R${salario}')
print(f'O desconto de imposto de renda foi de R${imposto_de_renda}')
print(f'O desconto de INSS foi de R${inss}')
print(f'O desconto de sindicato foi de R${sindicato}')

