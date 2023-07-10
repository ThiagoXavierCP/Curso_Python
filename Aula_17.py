# Operador lógico "and" (Todas as condições precisam ser verdadeiras)
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 0 0.0 e ' '
# None é usado para representar um não valor
#-----------------------------------
# Operador lógico "or" (Qualquer condição verdadeira avalia toda a expressão como verdadeira)
#-----------------------------------
# Operador lógico "not" (Usado para inverter expressões - not True = False / not False = True)
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou')
elif not senha_permitida:
    print('Senha incorreta')
else:
    print('')


   