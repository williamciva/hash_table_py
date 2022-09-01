from os import system

class Menu():

    def __init__(self):
        system('cls')
        print('Menu\n')
        print('Seja Bem vindo ao Sistema\n')
        

    def listar_opções(self):
        dic_menu = {    1 : 'Busca Completa do Veículo pela Placa',
                        2 : 'Buscar Veículo',
                        3 : 'Registrar Novo Veículo',
                        4 : 'Excluir Veículo',
                        5 : 'Mostrar Todos os Registros',
                    }
        
        for i in dic_menu:
            print(i,' - ',dic_menu.get(i))
        
        return 


    def get_opcao():
        opcao : int
        try:
            opcao = int(input('Opção Selecionada >>>   '))
            return opcao
        except ValueError as erro:
            system('cls')
            print('Por Favor Infrome Apenas Numeros Inteiros.\n')
            print('Erro  >>>  ', erro)
            input()