from veiculo.Placa import Placa

class Veiculo():
    marca : str
    modelo : str
    proprietario : str
    placa : Placa


    def __init__(self, 
                marca : str, 
                modelo : str, 
                proprietario : str,
                placa : Placa
                ):
        self.marca = marca
        self.modelo = modelo
        self.proprietario = proprietario
        self.placa = placa


    def __str__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)

    def __repr__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)