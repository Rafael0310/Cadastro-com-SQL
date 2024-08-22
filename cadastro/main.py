from connection import cursor
from db import ( 
    CREATE_DATABASE,
    CREATE_TABLE_USERS )

from metodos import (
    novo_usuario )

cursor.execute(CREATE_DATABASE)
cursor.execute(CREATE_TABLE_USERS)

while True:
    print('Sistema de cadastro\n\n1 - Cadastrar\n2 - Imprimir\n3 - Editar\n4 - Excluir\n5 - Sair\n')
    opc = int(input('O que deseja fazer? '))

    match opc:
        case 1:
            novo_usuario()

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            exit()

        case _:
            print('Opção inválida, tente novamente.')