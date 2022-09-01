def verifica_placa(letras_placa : str, numeros_placa : str):
    return True if letras_placa.isalpha() and len(letras_placa) == 3 and numeros_placa.isdigit() and len(numeros_placa) == 4 else False