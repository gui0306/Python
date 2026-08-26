''' Salario com comissão '''

import locale 
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor fixo = float(input("Salario fixo: "))
valor variavel = float(input("Total vendido: "))

comissao = totalVendido * 0.4
print = locale.currency(comissao, grouping=True, international=False)

salario atual = salarioFixo + comissao
print = locale.currency(salarioAtual, grouping=True, international=False)
