from veiculo.Veiculo import Veiculo
from converte_placa_ascii import converte_placa_ascii

def hash_func(veiculo : Veiculo):
    placa_completa = veiculo.placa.placa_completa
    placa_numeros = veiculo.placa.numeros
    placa_letras = veiculo.placa.letras

    converte_placa_ascii(placa_completa)