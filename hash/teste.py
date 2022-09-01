def converte_placa_para_ascii(placa):
    placa_ascii : str = ''
    for i in placa:
        placa_ascii = placa_ascii + str(ord(i))
    
    return int(placa_ascii) / 4

print('Placas PR:  ', converte_placa_para_ascii('AAA0001'), ' até ', converte_placa_para_ascii('BEZ9999'))
print('Placas MG:  ', converte_placa_para_ascii('GKJ0001'), ' até ', converte_placa_para_ascii('HOK9999'))
print('Placas RS:  ', converte_placa_para_ascii('IAQ0001'), ' até ', converte_placa_para_ascii('JDO9999'))
print('Placas PR:  ', converte_placa_para_ascii('JKS0001'), ' até ', converte_placa_para_ascii('JSZ9999'))