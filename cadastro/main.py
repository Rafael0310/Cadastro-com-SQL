from connection import cursor
from db import ( 
    CREATE_DATABASE,
    CREATE_TABLE_USERS,
    INSERT_USER )

cursor.execute(CREATE_DATABASE)
cursor.execute(CREATE_TABLE_USERS)

while True:
    print('Sistema de cadastro\n\n1 - Cadastrar\n2 - Imprimir\n3 - Editar\n4 - Excluir\n5 - Sair')
    opc = int(input('O que deseja fazer?'))

    match opc:
        case 1:
            