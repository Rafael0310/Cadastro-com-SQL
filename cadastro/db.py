CREATE_DATABASE = '''
CREATE DATABASE IF NOT EXISTS cadastro;
'''

CREATE_TABLE_USERS = '''
CREATE TABLE IF NOT EXISTS users (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    tel INT NOT NULL
);'''

INSERT_USER = '''
    INSERT INTO users (cpf, nome, tel) VALUES (%s, %s, %s)
'''