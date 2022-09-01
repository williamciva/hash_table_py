class Placa():
    letras : str
    numeros : int
    placa_completa : str

    def __init__(self, letras : str, numeros : str):
        self.letras = letras.upper()
        self.numeros = int(numeros)
        self.placa_completa = self.letras + numeros