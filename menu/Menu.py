from os import system
from hash.Hash_Table import Hash_Table
from veiculo.Placa import Placa
from veiculo.Veiculo import Veiculo
from veiculo.verifica_placa import verifica_placa

class Menu():
    __canto : str = '+'
    __borda  : str = '|'
    __titulo : str = '-'
    __descicao : str = ''
    __rodape : str = '-'

    def __init__(self):
        pass
        

    def listar_opções_iniciais(self):
        dic_menu = {    1 : 'Busca Completa do Veículo pela Placa',
                        2 : 'Buscar Veículo',
                        3 : 'Registrar Novo Veículo',
                        4 : 'Excluir Veículo',
                        5 : 'Mostrar Todos os Registros',
                        6 : 'Sair'
                    }
        
        for i in dic_menu:
            print(i,' - ',dic_menu.get(i))
        
        return 


    def buscar_veiculo(self, hash_table : Hash_Table):
        Menu.cabecalho(self, 'BUSCAR VEÍCULO', 'Informe os dados da placa que deseja consultar')
        letras_placa = input('Informe as LETRAS do emplacamento >>>   ')
        numeros_placa = input('Informe os NUMEROS do emplacamento >>>   ')


        if verifica_placa(letras_placa, numeros_placa) == True:
            placa = Placa(letras=letras_placa, numeros=numeros_placa)
            veiculo = Veiculo(marca='', modelo='', placa=placa, proprietario='')
            resposta = hash_table.get(veiculo)
            if isinstance(resposta, Veiculo):
                system('cls')
                Menu.cabecalho(self, 'VEICULO', resposta.placa.placa_completa)
                print('Marca >>>          ', resposta.marca)
                print('Modelo >>>         ', resposta.modelo)
                print('Proprietario >>>   ', resposta.proprietario)
                print('Placa >>>          ', resposta.placa.placa_completa)
                input('\n Pressione qualquer tecla...')
                return  
            else:
                system('cls')
                print('Não existem veículos cadastrados com a placa: ', placa.letras, placa.numeros)
                input('\nPressione qualquer tecla...')
                return  
        else:
                system('cls')
                print('Erro ao consular o Veículo:\n')
                print('Erro >>>   ', 'A placa informada é inválida!!')
                input('\n Pressione qualquer tecla...')
                return  


    def buscar_veiculo_consulta_restrita(self, hash_table : Hash_Table):
        Menu.cabecalho(self, 'BUSCAR VEÍCULO', 'Informe os dados da placa que deseja consultar')
        letras_placa = input('Informe as LETRAS do emplacamento >>>   ')
        numeros_placa = input('Informe os NUMEROS do emplacamento >>>   ')


        if verifica_placa(letras_placa, numeros_placa) == True:
            placa = Placa(letras=letras_placa, numeros=numeros_placa)
            veiculo = Veiculo(marca='', modelo='', placa=placa, proprietario='')
            resposta = hash_table.get(veiculo)
            if isinstance(resposta, Veiculo):
                system('cls')
                Menu.cabecalho(self, 'VEICULO', resposta.placa.placa_completa)
                print('Veículo Encontrado!!\n')
                input('\n Pressione qualquer tecla...')
                Menu.cabecalho(self, 'VEICULO', resposta.placa.placa_completa)
                while True:
                    system('cls')
                    print('Que dados deseja vizualizar?')
                    print('1 - Marca\n2 - Modelo\n3 - Proprietario\n4 - Placa\n5 - Sair')
                    opcao =  Menu.get_opcao()       
                    if opcao == 1:
                        system('cls')         
                        print('Marca >>>          ', resposta.marca)
                    elif opcao == 2:
                        system('cls')
                        print('Modelo >>>         ', resposta.modelo)
                    elif opcao == 3:
                        system('cls')
                        print('Proprietario >>>   ', resposta.proprietario)
                    elif opcao == 4:
                        system('cls')
                        print('Placa >>>          ', resposta.placa.placa_completa)
                    elif opcao == 5:
                        break
                    else:
                        print('Opção Inválida!')

                    input('\n Pressione qualquer tecla...')
                return  
            else:
                system('cls')
                print('Não existem veículos cadastrados com a placa: ', placa.letras, placa.numeros)
                input('\nPressione qualquer tecla...')
                return  
        else:
                system('cls')
                print('Erro ao consular o Veículo:\n')
                print('Erro >>>   ', 'A placa informada é inválida!!')
                input('\n Pressione qualquer tecla...')


    def registrar_veiculo(self, hash_table : Hash_Table):
            Menu.cabecalho(self, 'REGISTRAR VEÍCULO', 'Informe os dados necessários.')
            marca = input('Informe a marca >>>   ')
            modelo = input('Informe o modelo >>>   ')
            proprietario = input('Informe o proprietario >>>   ')
            letras_placa = input('Informe as LETRAS do emplacamento >>>   ')
            numeros_placa = input('Informe os NUMEROS do emplacamento >>>   ')

            
            if verifica_placa(letras_placa, numeros_placa) == True:
                placa = Placa(letras=letras_placa, numeros=numeros_placa)
                veiculo = Veiculo(marca=marca, modelo=modelo, placa=placa, proprietario=proprietario)
                resposta = hash_table.put(veiculo)
                try:
                    int(resposta)
                    print('Veículo registrado com sucesso na posição: ', resposta)
                    input('\n Pressione qualquer tecla...')
                    return  
                except ValueError:
                    system('cls')
                    print('Erro ao registrar o Veículo:\n')
                    print('Erro >>>   ', resposta)
                    input('\nPressione qualquer tecla...')
                    return  
            else:
                system('cls')
                print('Erro ao registrar o Veículo:\n')
                print('Erro >>>   ', 'A placa informada é inválida!!')
                input('\n Pressione qualquer tecla...')
                return


    def excluir_veiculo(self, hash_table : Hash_Table):
        Menu.cabecalho(self, 'Excluir Veículo', 'Informe os dados da placa que deseja excluir')
        letras_placa = input('Informe as LETRAS do emplacamento >>>   ')
        numeros_placa = input('Informe os NUMEROS do emplacamento >>>   ')


        if verifica_placa(letras_placa, numeros_placa) == True:
            placa = Placa(letras=letras_placa, numeros=numeros_placa)
            veiculo = Veiculo(marca='', modelo='', placa=placa, proprietario='')
            system('cls')
            print(hash_table.pop(veiculo))
            input('\n Pressione qualquer tecla...')
            return
        else:
            system('cls')
            print('Erro ao regexcluir o Veículo:\n')
            print('Erro >>>   ', 'A placa informada é inválida!!')
            input('\n Pressione qualquer tecla...')
            return


    def consulta_completa(self, hash_table : Hash_Table):
        dict = hash_table.get_all()

        system('cls')
        for i in dict.keys():
            print('--------------------------------------------------------------')
            print('Estado >>>  ',i)
            for j in dict[i]:
                print('           ---------------------------------------------------')
                print('             Placa >>>          ', j.placa.placa_completa)
                print('             Marca >>>          ', j.marca)
                print('             Modelo >>>         ', j.modelo)
                print('             Proprietario >>>   ', j.proprietario)
                
    
        input('\n Pressione qualquer tecla...')


    def get_opcao():
        opcao : int
        try:
            opcao = int(input('\nOpção Selecionada >>>   '))
            return opcao
        except ValueError as erro:
            system('cls')
            print('Por favor, infrome apenas numeros INTEIROS.\n')
            print('Erro >>>   ', erro)
            input('\nPressione qualquer tecla...')


    def cabecalho(self, titulo : str, descicao):
        tamanho_max = len(titulo) + 14  if descicao < titulo else len(descicao) + 14
            
            
        metade_da_descicao = (tamanho_max - len(descicao))//2
        metade_do_titulo = (tamanho_max - len(titulo)-2)//2 
        

        self.__titulo = self.__canto
        self.__descicao = self.__borda
        self.__rodape = self.__canto

        for i in range(1,metade_da_descicao):
            self.__descicao = self.__descicao + ' '
            
        for i in range(1,metade_do_titulo):
            self.__titulo = self.__titulo + '-'

        self.__titulo = self.__titulo + ' '+ titulo + ' '    
        self.__descicao = self.__descicao + descicao


        for i in range(len(self.__descicao),tamanho_max-1):
            self.__descicao = self.__descicao + ' '

        for i in range(len(self.__titulo),tamanho_max-1):
            self.__titulo = self.__titulo + '-'

        for i in range(1,tamanho_max-1):
            self.__rodape = self.__rodape + '-'

        self.__titulo = self.__titulo + self.__canto
        self.__descicao = self.__descicao + self.__borda
        self.__rodape = self.__rodape + self.__canto

        system('cls')
        print(self.__titulo + '\n' + self.__descicao + '\n' + self.__rodape + '\n\n')
        return