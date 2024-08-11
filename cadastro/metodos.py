import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def novo_usuario():
    limpar_tela()
    while True:
        try:
            cpf = int(input('Insira o CPF: '))
            nome = input('Digite o nome: ')
            tel = int('Digite o telefone: ')
        except ValueError:
            print('Por favor, insira valores inteiros.')