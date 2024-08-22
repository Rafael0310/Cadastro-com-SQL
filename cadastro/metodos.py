# Import Database e Metodos
from connection import cursor
from db import INSERT_USER

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def novo_usuario():
    limpar_tela()
    while True:
        cpf = input('Insira o CPF: ')

        if len(cpf) == 11:
            try:
                nome = input('Digite o nome: ')
                tel = int(input('Digite o telefone: '))
                cursor.execute(INSERT_USER, (cpf, nome, tel))

            except ValueError:
                print('Por favor, insira valores inteiros.')

        else:
            print('Formato do CPF inválido')