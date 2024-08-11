CREATE_DATABASE = '''
CREATE DATABASE IF NOT EXISTS cadastro;
'''

CREATE_TABLE_USERS = '''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf INT UNIQUE,
    nome VARCHAR(255) NOT NULL,
    tel INT NOT NULL
);'''

INSERT_USER = '''
    INSERT INTO users (id, cpf, nome, tel) VALUES (%s, %s, %s, %s)
'''