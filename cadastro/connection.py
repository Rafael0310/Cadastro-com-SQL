import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='cadastro',
    user='root',
    password='Iva@Mj#031015'
)

cursor = conn.cursor()