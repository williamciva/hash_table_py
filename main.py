from os import system
from menu.Menu import Menu
from hash.Hash_Table import Hash_Table


hash_table = Hash_Table()
while True:
    Menu().cabecalho('MENU PRINCIPAL','Seja bem vindo ao sistema!!')
    Menu().listar_opções_iniciais()
    opcao = Menu.get_opcao()

    if opcao == 1:
        Menu().buscar_veiculo(hash_table)
    elif opcao == 2:
        Menu().buscar_veiculo_consulta_restrita(hash_table)
    elif opcao == 3:
        Menu().registrar_veiculo(hash_table)
    elif opcao == 4:
        Menu().excluir_veiculo(hash_table)
    elif opcao == 5:
        Menu().consulta_completa(hash_table)
    elif opcao == 6:
        system('cls')
        break
    else:
        system('cls')
        print('Opção Inválida!')
        input('\nPressione qualquer tecla...')