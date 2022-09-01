def converte_placa_ascii(placa):
    placa_ascii : str = ''
    for i in placa:
        placa_ascii = placa_ascii + str(ord(i))
    
    return int(placa_ascii)