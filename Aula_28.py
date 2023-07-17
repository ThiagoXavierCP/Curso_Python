"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

#------------------------------------------------------------

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')