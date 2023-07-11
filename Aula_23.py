"""
Introdução ao Try/Except
Try-> tentar executar o código
Except -> Ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero digitado: ')

try:
    print('STR:', numero_str)
    numero_float = float (numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:}')
except: 
    print('Isso não é um número')