"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições do mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

#Velocidade do carro acima do radar
vel_car_pass = velocidade > RADAR_1
carro_passou_r1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_r1 = carro_passou_r1 and vel_car_pass

if vel_car_pass:
    print('Velocidade do carro acima do limite permitido do radar 1')

if carro_passou_r1:
    print('Carro passou no radar 1')

if carro_passou_r1 and vel_car_pass:
    print('Carro multado em radar 1')