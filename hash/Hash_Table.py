from hash.Bucket import Bucket
from hash.Hash_Map import Hash_Map
from veiculo.Veiculo import Veiculo
from hash.converte_placa_ascii import converte_placa_ascii

class Hash_Table(Hash_Map):
    # Essa classe realiza o controle dos veículos armazenando-os em
    # buckets por seus respectivos estados pré definidos no construtor.
    # Essa classe conta com os métodos mais comuns presentes em hash tables.

    Bucket_PR : Bucket
    Bucket_MG : Bucket
    Bucket_RS : Bucket
    Bucket_BA : Bucket


    def __init__(self):
        self.Bucket_PR = Bucket('Bucket_PR', bucket_id=1)
        self.Bucket_MG = Bucket('Bucket_MG', bucket_id=2)
        self.Bucket_RS = Bucket('Bucket_RS', bucket_id=3)
        self.Bucket_BA = Bucket('Bucket_BA', bucket_id=4)


    def hash_func(self, veiculo : Veiculo):
        placa_completa = veiculo.placa.placa_completa

        ascii = converte_placa_ascii(placa_completa)
        
        if ascii in range(converte_placa_ascii('AAA0001'), converte_placa_ascii('BEZ9999') + 1):
            return self.Bucket_PR

        if ascii in range(converte_placa_ascii('GKJ0001'), converte_placa_ascii('HOK9999') + 1):
            return self.Bucket_MG

        if ascii in range(converte_placa_ascii('IAQ0001'), converte_placa_ascii('JDO9999') + 1):
            return self.Bucket_RS

        if ascii in range(converte_placa_ascii('JKS0001'), converte_placa_ascii('JSZ9999') + 1):
            return self.Bucket_BA

        else:
            return 'A placa informada não pode ser registrada em nem um dos UF''s disponíveis.'


    def put(self, veiculo : Veiculo):
        bucket = Hash_Table.hash_func(self, veiculo)
        try:
            for i in bucket.bucket_vector:
                if i.placa.placa_completa == veiculo.placa.placa_completa:
                    return 'O veículo ja está registrado.'
        except AttributeError:
            return bucket

        bucket.bucket_vector.append(veiculo)
        return bucket.bucket_vector.index(veiculo)


    def get(self, veiculo : Veiculo ) -> Veiculo:
        bucket = Hash_Table.hash_func(self, veiculo)
        try:
            for i in bucket.bucket_vector:
                if i.placa.placa_completa == veiculo.placa.placa_completa:
                    return i
            return 'O veículo não existe no sistema'
        except ValueError:
            return 'O veículo não existe no sistema'
        except AttributeError:
            return bucket


    def pop(self, veiculo : Veiculo):
        bucket = Hash_Table.hash_func(self, veiculo)
        try:
            for i in bucket.bucket_vector:
                if i.placa.placa_completa == veiculo.placa.placa_completa:
                    index = bucket.bucket_vector.index(i)
                    bucket.bucket_vector.pop(index)
                    return 'Item removido com sucesso!!'
            return 'O veículo não existe no sistema'
        except ValueError:
            return 'O veículo não existe no sistema'
        except AttributeError:
            return 'O veículo não existe no sistema'


    def contains(self, veiculo : Veiculo):
        bucket = Hash_Table.hash_func(self, veiculo)
        return bucket.bucket_vector.__contains__(veiculo)
        
    
    def count(self, veiculo : Veiculo):
        bucket = Hash_Table.hash_func(self, veiculo)
        return bucket.bucket_vector.__len__()

    def get_all(self):
        retorno = {}

        Bucket_PR = []
        for i in self.Bucket_PR.bucket_vector:
            Bucket_PR.append(i)
        retorno[self.Bucket_PR.bucket_name] = Bucket_PR

        Bucket_MG = []
        for i in self.Bucket_MG.bucket_vector:
            Bucket_MG.append(i)
        retorno[self.Bucket_MG.bucket_name] = Bucket_MG

        Bucket_RS = []
        for i in self.Bucket_RS.bucket_vector:
            Bucket_RS.append(i)
        retorno[self.Bucket_RS.bucket_name] = Bucket_RS

        Bucket_BA = []
        for i in self.Bucket_BA.bucket_vector:
            Bucket_BA.append(i)
        retorno[self.Bucket_BA.bucket_name] = Bucket_BA

        return retorno