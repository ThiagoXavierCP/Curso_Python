nome = 'Thiago'
altura = 1.79
peso = 73
imc = peso / altura ** 2 

"f-strings"
linha_1 = f'{nome} tem {altura:,.2F} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2F}'

print(linha_1)
print(linha_2)
print(linha_3)