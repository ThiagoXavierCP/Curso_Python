"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num_inteiro = input('Digite um numero inteiro: ')
if num_inteiro.isdigit():
    num_inteiro = int (num_inteiro)
    par_impar = num_inteiro % 2 == 0
    par_impar_texto = 'Ímpar'

    if par_impar:
        par_impar_texto = 'Par'

    print(f'O numero {num_inteiro} é {par_impar_texto}.')
else:
    print('Você não digitou um numero inteiro')


"""
Faça um programa que eprgunte a hora ao usuário e, baseando-se no horário desrito, exiba a saudação apropriada.Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horas = float(input('Digite as horas: '))

if horas >= 00 and horas <= 11:
    print('Bom dia!')

elif horas >= 12 and horas <= 17:
    print('Boa tarde!')

elif horas >= 18 and horas <= 23:
    print('Boa noite!')

else: 
    print('Horas Invalidas')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite seu primeiro nome: ')

if {len(nome)} >= 4:
    print('Seu nome é curto')

elif {len(nome)} >= 5 and {len(nome)} <= 6:
    print('Seu nome é normal')

else: 
    print('Seu nome é muito grande') 